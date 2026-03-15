---

# Week Calculator & iCalendar Generator

一个简单的 **Python 周数计算器和 iCalendar 生成工具**。
输入起始日期和终止日期，程序会：

1. 计算该时间范围内的所有周
2. 显示每周的开始和结束日期
3. 生成 `.ics` 日历文件
4. 可直接导入 **Apple Calendar / Google Calendar / Outlook**

适用于：

* 学期周数安排
* 项目周期规划
* 课程表周计划
* 个人时间管理

---

# Features

* 支持 **多种日期格式输入**
* 自动计算 **周一到周日的周范围**
* 自动生成 **iCalendar (.ics) 文件**
* 支持 **全天事件**
* 可直接导入主流日历软件
* 无第三方依赖（纯 Python 标准库）

---

# Supported Date Formats

程序支持多种常见日期格式：

```
YYYY-MM-DD   -> 2024-01-01
YYYY/MM/DD   -> 2024/01/01
DD/MM/YYYY   -> 01/01/2024
DD-MM-YYYY   -> 01-01-2024
MM/DD/YYYY   -> 01/01/2024
MM-DD-YYYY   -> 01-01-2024
```

示例：

```
2024-03-01
2024/3/1
1/3/2024
```

---

# Installation

克隆仓库：

```bash
git clone https://github.com/yourusername/week-calculator.git
cd week-calculator
```

本项目 **无需安装任何依赖**。

只需要 Python 3.7+

检查 Python：

```bash
python --version
```

---

# Usage

运行程序：

```bash
python week_calculator.py
```

程序会提示输入日期：

```
=== Week Calculator and Calendar Generator ===

Enter start date: 2024-03-01
Enter end date: 2024-06-30
```

输出示例：

```
From 2024-03-01 to 2024-06-30 there are 18 weeks

Week details:
Week 1: 2024-03-01 - 2024-03-03
Week 2: 2024-03-04 - 2024-03-10
Week 3: 2024-03-11 - 2024-03-17
...
```

随后生成文件：

```
weeks_2024-03-01_2024-06-30.ics
```

---

# Importing the Calendar

生成的 `.ics` 文件可以导入日历。

### Apple Calendar

方法 1：

```
双击 .ics 文件
```

方法 2：

```
Calendar → File → Import → 选择 .ics 文件
```

---

### Google Calendar

1. 打开 Google Calendar
2. 点击 **Settings**
3. 选择 **Import & Export**
4. 上传 `.ics` 文件

---

### Outlook

```
File → Open & Export → Import/Export → Import an iCalendar file
```

---

# Project Structure

```
week-calculator
│
├── week_calculator.py    # 主程序
└── README.md             # 项目说明
```

---

# Example Generated Event

生成的日历事件示例：

```
Week 1
03月01日 - 03月03日
All Day Event
```

---

# Possible Improvements

未来可以扩展：

* CLI 参数模式（无需交互输入）
* 自定义周起始日
* 生成课程表
* GUI 版本
* 自动导入日历
* Web 版本

---

# License

MIT License

---
