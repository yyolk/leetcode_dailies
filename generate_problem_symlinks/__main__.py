"""Generate solution symlinks in solutions/zz_by_problem_number."""

from .utils import (
    BASE_SOLUTIONS_DIR,
    BY_PROBLEM_DIR,
    clear_symlink_dir,
    extract_problem_number,
    iter_solution_files,
)


def main():
    """Generate links named <PROBLEM NUMBER>_YYYYMMDD.ext."""
    BY_PROBLEM_DIR.mkdir(parents=True, exist_ok=True)
    clear_symlink_dir(BY_PROBLEM_DIR)

    generated_count = 0
    skipped_count = 0

    for solution_file in iter_solution_files(BASE_SOLUTIONS_DIR):
        problem_number = extract_problem_number(solution_file)
        if problem_number is None:
            skipped_count += 1
            print(f"Skipping {solution_file}: no problem number found")
            continue

        relative_target = solution_file.relative_to(BASE_SOLUTIONS_DIR)
        link_name = f"{problem_number}_{solution_file.stem}{solution_file.suffix}"
        link_path = BY_PROBLEM_DIR / link_name
        link_path.symlink_to(".." / relative_target)
        generated_count += 1

    print(f"Generated {generated_count} symlinks in {BY_PROBLEM_DIR}")
    if skipped_count:
        print(f"Skipped {skipped_count} files without problem number metadata")


if __name__ == "__main__":
    main()
