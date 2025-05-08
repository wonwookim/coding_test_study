import requests
import re
from pathlib import Path

README_PATH = Path("README.md")
SOLVEDAC_API = "https://solved.ac/api/v3/search/problem"
HEADERS = {"x-solvedac-language": "ko"}

problem_titles = ['예산', '공유기 설치', '주식', '병든 나이트']
tech_type = "이분탐색, 그리디 알고리즘"
WORKBOOK_URL = ""

def get_problem_info(title):
    params = {"query": title, "sort": "id", "direction": "asc"}
    response = requests.get(SOLVEDAC_API, headers=HEADERS, params=params)
    data = response.json()
    item = data['items'][0]
    return {
        "title": item["titleKo"],
        "problemId": item["problemId"],
        "level": item["level"]
    }

def get_next_week_number(readme_lines):
    weeks = [int(m.group(1)) for line in readme_lines if (m := re.search(r"Week (\d+)", line))]
    return max(weeks) + 1 if weeks else 1

def make_github_link(problemId, title, week):
    folder_name = f"{problemId}_{title.replace(' ', '_')}"
    encoded_folder = requests.utils.quote(folder_name)
    return f"https://github.com/wonwookim/coding_test_study/tree/main/week_{week}/{encoded_folder}"

def create_problem_folders(problem_data, week, base_path):
    created = []
    for p in problem_data:
        folder_name = f"{p['problemId']}_{p['title'].replace(' ', '_')}"
        full_path = Path(base_path) / f"week_{week}" / folder_name
        full_path.mkdir(parents=True, exist_ok=True)
        readme_path = full_path / "README.md"
        if not readme_path.exists():
            readme_path.write_text(f"# {p['title']} 문제 풀이\n\n백준 문제 번호: {p['problemId']}", encoding="utf-8")
        created.append(str(full_path))
    return created

def merge_block_to_summary(block_lines):
    titles, levels = [], []
    week = None
    tech_type = None
    for line in block_lines:
        match = re.findall(r"\|\s*Week (\d+)\s*\|\s*(.*?)\|\s*\[(.*?)\]\((.*?)\)\s*\|\s*<img.*?/(\d+).svg.*?>", line)
        if match:
            w, tech, title, url, level = match[0]
            week = w
            tech_type = tech
            titles.append(f"[{title}]({url})")
            levels.append(f"<img src=\"https://static.solved.ac/tier_small/{level}.svg\" width=\"30\" height=\"30\">")
    if not week:
        return None
    merged = f"| Week {week} | {tech_type} | {'<br>'.join(titles)} | {'<br>'.join(levels)} | {'<br>'.join(['✅']*len(titles))} | [바로가기](https://github.com/wonwookim/coding_test_study/tree/main/week_{week}) |\n"
    return merged

def insert_to_record_table(readme_lines, new_row):
    start_idx, end_idx = None, None
    for i, line in enumerate(readme_lines):
        if "## 🏆 문제 풀이 기록" in line:
            start_idx = i
        elif start_idx is not None and line.strip().startswith("|-------"):
            end_idx = i + 1
            break
    for i in range(end_idx, len(readme_lines)):
        if not readme_lines[i].strip().startswith("|"):
            table_end = i
            break
    else:
        table_end = len(readme_lines)
    return readme_lines[:table_end] + [new_row + "\n"] + readme_lines[table_end:]


def extract_current_week_block(readme_lines):
    start = end = None
    for i, line in enumerate(readme_lines):
        if "## 📌 이번 주 문제" in line:
            start = i
        elif start is not None and line.startswith("## "):
            end = i
            break
    if end is None:
        end = len(readme_lines)
    return start, end, readme_lines[start+3:end]  # skip title, 문제집, header

def make_markdown_table(problem_data, week):
    table = [
        "| 주차  | 기술 유형     | 문제명  | 난이도 | 풀이<br>여부 | 풀이<br>링크 |",
        "|-------|---------------|:--------:|:------:|:-----------:|:-----------:|"
    ]
    for p in problem_data:
        row = (
            f"| Week {week} | {tech_type} | "
            f"[{p['title']}](https://www.acmicpc.net/problem/{p['problemId']}) | "
            f"<img src=\"https://static.solved.ac/tier_small/{p['level']}.svg\" width=\"30\" height=\"30\"> | ⬜ | "
            f"[바로가기]({make_github_link(p['problemId'], p['title'], week)}) |"
        )
        table.append(row)
    return [line + "\n" for line in table]


def main():
    readme_lines = README_PATH.read_text(encoding="utf-8").splitlines(keepends=True)
    week = get_next_week_number(readme_lines)
    problems = [get_problem_info(title) for title in problem_titles]
    folders = create_problem_folders(problems, week, ".")

    # 백업용 현재 문제 블록 추출 → 기록용 한 줄 요약
    start, end, current_block = extract_current_week_block(readme_lines)
    summary_line = merge_block_to_summary(current_block)
    if summary_line:
        readme_lines = insert_to_record_table(readme_lines, summary_line)

    # 이번 주 문제 영역에 새 주차 테이블 삽입
        # replace 문제집 링크
    for i, line in enumerate(readme_lines):
        if "🔗 **이번 주 문제집:**" in line:
            readme_lines[i] = f"🔗 **이번 주 문제집:** [백준 문제집]({WORKBOOK_URL})\n"
            break

    new_table = make_markdown_table(problems, week)
    updated_lines = readme_lines[:start+3] + new_table + ["\n"] + readme_lines[end:]
    README_PATH.write_text("".join(updated_lines), encoding="utf-8")

    print("✅ README.md 업데이트 완료")
    print("📁 생성된 폴더:")
    for f in folders:
        print("-", f)

if __name__ == "__main__":
    main()