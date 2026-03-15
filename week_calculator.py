#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
周数计算器和iCalendar生成器
输入起始日期和终止日期，计算周数并生成ICS文件导入到苹果日历
"""

import datetime
import uuid
from typing import List, Tuple


class WeekCalculator:
    def __init__(self):
        self.events = []
    
    def parse_date(self, date_str: str) -> datetime.date:
        """解析日期字符串，支持多种格式"""
        formats = [
            '%Y-%m-%d',
            '%Y/%m/%d',
            '%d/%m/%Y',
            '%d-%m-%Y',
            '%m/%d/%Y',
            '%m-%d-%Y'
        ]
        
        for fmt in formats:
            try:
                return datetime.datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
        
        raise ValueError(f"无法解析日期: {date_str}")
    
    def calculate_weeks(self, start_date: datetime.date, end_date: datetime.date) -> List[Tuple[datetime.date, datetime.date, int]]:
        """计算指定日期范围内的所有周"""
        if start_date > end_date:
            raise ValueError("起始日期必须早于或等于终止日期")
        
        weeks = []
        current_date = start_date
        week_number = 1
        
        while current_date <= end_date:
            # 计算当前周的开始（周一）和结束（周日）
            week_start = current_date - datetime.timedelta(days=current_date.weekday())
            week_end = week_start + datetime.timedelta(days=6)
            
            # 确保不超出范围
            if week_start < start_date:
                week_start = start_date
            if week_end > end_date:
                week_end = end_date
            
            # 如果这一周有有效日期，添加到列表
            if week_start <= week_end:
                weeks.append((week_start, week_end, week_number))
            
            # 移动到下一周
            current_date = week_start + datetime.timedelta(days=7)
            week_number += 1
            
            # 防止无限循环
            if week_number > 1000:
                raise ValueError("日期范围过大，请检查输入")
        
        return weeks
    
    def create_calendar_event(self, week_start: datetime.date, week_end: datetime.date, week_number: int) -> dict:
        """创建日历事件"""
        return {
            'uid': str(uuid.uuid4()),
            'summary': f'第{week_number}周',
            'description': f'第{week_number}周 ({week_start.strftime("%m月%d日")} - {week_end.strftime("%m月%d日")})',
            'start_date': week_start,
            'end_date': week_end,
            'all_day': True
        }
    
    def generate_ics_content(self, weeks: List[Tuple[datetime.date, datetime.date, int]]) -> str:
        """生成ICS文件内容"""
        events = []
        
        for week_start, week_end, week_number in weeks:
            event = self.create_calendar_event(week_start, week_end, week_number)
            
            # 构建iCalendar事件格式
            dtstamp = datetime.datetime.now().strftime('%Y%m%dT%H%M%SZ')
            dtstart = week_start.strftime('%Y%m%d')
            dtend = (week_end + datetime.timedelta(days=1)).strftime('%Y%m%d')  # ICS结束日期是次日
            
            event_content = f"""BEGIN:VEVENT
UID:{event['uid']}
DTSTAMP:{dtstamp}
DTSTART;VALUE=DATE:{dtstart}
DTEND;VALUE=DATE:{dtend}
SUMMARY:{event['summary']}
DESCRIPTION:{event['description']}
STATUS:CONFIRMED
TRANSP:TRANSPARENT
END:VEVENT"""
            
            events.append(event_content)
        
        # 构建完整的ICS文件
        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//周数计算器//CN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:周数计划
X-WR-TIMEZONE:Asia/Shanghai
{chr(10).join(events)}
END:VCALENDAR"""
        
        return ics_content
    
    def save_ics_file(self, ics_content: str, filename: str = "weeks_schedule.ics"):
        """保存ICS文件"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(ics_content)
            print(f"ICS file saved: {filename}")
            return True
        except Exception as e:
            print(f"File save failed: {e}")
            return False
    
    def run(self):
        """运行主程序"""
        print("=== Week Calculator and Calendar Generator ===")
        print("Supported date formats: 2024-01-01, 2024/1/1, 1/1/2024, etc.")
        print()
        
        try:
            # 获取用户输入
            start_input = input("Enter start date: ").strip()
            end_input = input("Enter end date: ").strip()
            
            # 解析日期
            start_date = self.parse_date(start_input)
            end_date = self.parse_date(end_input)
            
            # 计算周数
            weeks = self.calculate_weeks(start_date, end_date)
            
            print(f"\nFrom {start_date} to {end_date} there are {len(weeks)} weeks")
            
            # 显示周信息
            print("\nWeek details:")
            for week_start, week_end, week_number in weeks:
                print(f"Week {week_number}: {week_start} - {week_end}")
            
            # 生成ICS文件
            ics_content = self.generate_ics_content(weeks)
            
            # 保存文件
            filename = f"weeks_{start_date}_{end_date}.ics"
            if self.save_ics_file(ics_content, filename):
                print(f"\n📅 Calendar file generated: {filename}")
                print("💡 Usage instructions:")
                print("   1. Double-click the ICS file to import to Apple Calendar")
                print("   2. Or in Calendar app select File > Import > Choose this file")
                print("   3. Can choose to create new calendar or add to existing calendar")
            
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    """主函数"""
    calculator = WeekCalculator()
    calculator.run()


if __name__ == "__main__":
    main()