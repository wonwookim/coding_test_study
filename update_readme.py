import requests
import re
from pathlib import Path

# 기본 설정
README_PATH = Path("README.md")
HEADERS = {"x-solvedac-language": "ko"}
SOLVEDAC_API_SHOW = "https://solved.ac/api/v3/problem/show"

# 📌 사용자 설정
problem_ids = [1074, 1931, 7576]  # 사용할 문제 번호 리스트
tech_type = "solved.ac stage_3"
WORKBOOK_URL = ""  # 백준 문제집 링크 입력 (필요시)

# 문제 번호 기반 정보 조회
def get_problem_info_by_id(problem_id):
    url = f"{SOLVEDAC_API_SHOW}?problemId={problem_id}"
    response = requests.get(url, headers=HEADERS)
    data = response.json()
    return {
        "title": data["titleKo"],
        "problemId": data["problemId"],
        "level": data["level"]
    }

# README에서 다음 주차 번호 추출
def get_next_week_number(readme_lines):
    weeks = [int(m.group(1)) for line in readme_lines if (m := re.search(r"Week (\d+)", line))]
    return max(weeks) + 1 if weeks else 1

# GitHub 링크 생성
def make_github_link(problemId, title, week):
    folder_name = f"{problemId}_{title.replace(' ', '_')}"
    encoded_folder = requests.utils.quote(folder_name)
    return f"https://github.com/wonwookim/coding_test_study/tree/main/week_{week}/{encoded_folder}"

# 문제 폴더 및 README.md 생성
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

# 현재 주차 블록 요약 → 한 줄 요약 테이블
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

# 기록 테이블에 한 줄 추가
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

# 📌 이번 주 문제 영역 추출
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

# Markdown 테이블 생성
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

# 메인 실행 함수
def main():
    readme_lines = README_PATH.read_text(encoding="utf-8").splitlines(keepends=True)
    week = get_next_week_number(readme_lines)
    problems = [get_problem_info_by_id(pid) for pid in problem_ids]
    folders = create_problem_folders(problems, week, ".")

    # 현재 블록을 기록 테이블에 요약 추가
    start, end, current_block = extract_current_week_block(readme_lines)
    summary_line = merge_block_to_summary(current_block)
    if summary_line:
        readme_lines = insert_to_record_table(readme_lines, summary_line)

    # 문제집 링크 업데이트
    for i, line in enumerate(readme_lines):
        if "🔗 **이번 주 문제집:**" in line:
            readme_lines[i] = f"🔗 **이번 주 문제집:** [백준 문제집]({WORKBOOK_URL})\n"
            break

    # 새로운 주차 테이블 삽입
    new_table = make_markdown_table(problems, week)
    updated_lines = readme_lines[:start+3] + new_table + ["\n"] + readme_lines[end:]
    README_PATH.write_text("".join(updated_lines), encoding="utf-8")

    print("✅ README.md 업데이트 완료")
    print("📁 생성된 폴더:")
    for f in folders:
        print("-", f)

if __name__ == "__main__":
    main()
