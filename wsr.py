"""
File  :    wsr.py
Author:    ershan
mail  :    ershan_coding@outlook.com
desc  :    1. Add contents to wsr
           2. Show contents in wsr

           - cli
           Usage: wsr.py [OPTIONS] [CONTENT]

            Options:
            --ls             List current contents in this week.
            --nu             Show the line number or not.
            -la, --list-all  List all reports.
            -e, --editor     Open a editor to append new contents.
            --help           Show this message and exit.

           - Listary
           double ctrl
           wsr*
"""


import os
import datetime
from pathlib import Path

import click


def get_info():
    """Get year and week.

    Returns:
        tuple[int]: year, week
    """
    now = datetime.datetime.now()
    year = now.year
    now = now.strftime("%Y%m%d")
    week = datetime.datetime.strptime(now, "%Y%m%d").strftime("%W")
    return year, week


def list_content(path, show_nu=False):
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if show_nu:
                print(f"{i}. {line}", end="")
            else:
                print(f"{line}", end="")
    input()


def append_data(content: str, add_date: bool = False):
    """Append new content to wsr file.

    Args:
        content (str): _description_
    """
    with open(wsr_path, "a", encoding="utf-8") as f:
        line = content + "\n"
        if add_date:
            today = datetime.date.today()
            date = today.strftime("%Y-%m-%d")
            line = f"{date}: {content}\n"
        if line.strip():
            f.write(line)


def get_index_of_summary():
    """Get line index of summary in wsr file."""
    wsr_path = "./2022-18.txt"
    with open(wsr_path, encoding="utf-8") as f:
        li = f.readlines()

    line_num = -1
    for i, line in enumerate(li):
        if line.startswith("总结"):
            line_num = i

    return line_num


def append_summary(content: str, add_date: bool, index: int):
    """Append content to summary part.

    Args:
        content (str): Content to add.
        add_date (bool): Whether add date or not.
        index (int): Line index of summary.
    """
    with open(wsr_path, encoding="utf-8") as f:
        li = f.readlines()

    li.append(content + "\n")


file = Path() / __file__
folder = file.parent
year, week = get_info()
wsr_path = folder / f"{year}-{week}.txt"


@click.command()
@click.argument("CONTENT", default="")
@click.option("--ls", help="List current contents in this week.", is_flag=True)
@click.option("--nu", help="Show the line number or not.", is_flag=True)
@click.option("--list-all", "-la", help="List all reports.", is_flag=True)
@click.option("--add-date", "-ad", help="Add date before content.", is_flag=True)
@click.option("--summary", "-s", help="Add to summary part.", is_flag=True)
@click.option(
    "--editor", "-e", help="Open a editor to append new contents.", is_flag=True
)
def wsr(content, ls, nu, list_all, editor, add_date, summary):
    if not wsr_path.exists():
        with open(wsr_path, "w", encoding="utf-8") as f:
            pass

    if summary:
        # 没有总结先加一个总结
        if (index := get_index_of_summary()) == -1:
            append_data("\n总结")
        append_data(content, add_date)
        return

    append_data(content, add_date)

    if ls:
        list_content(wsr_path, nu)
        return

    if list_all:
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                print(file)

    if editor:
        os.system(f"notepad {wsr_path}")


if __name__ == "__main__":
    wsr()
