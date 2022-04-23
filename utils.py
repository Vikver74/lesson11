import json, os.path


def load_candidates_from_json():
    """
    возвращает список всех кандидатов
    """
    path_to_json = os.path.join("data", "candidates.json")
    with open(path_to_json, "r", encoding="UTF-8") as file:
        return json.load(file)


def get_candidate(candidates, candidate_id):
    """
    возвращает одного кандидата по его id
    """
    for record in candidates:
        if record['id'] == candidate_id:
            return record


def get_candidates_by_age(candidates, candidate_age):
    """
    возвращает список кандидатов по возрасту age
    """
    candidates_by_age = []
    for record in candidates:
        if record['age'] == candidate_age:
            candidates_by_age.append(record)
    return candidates_by_age


def get_candidates_by_skills(candidates, skill_name):
    """
    возвращает список кандидатов по наличию skill
    """
    candidates_by_skill = []
    for record in candidates:
        skills_list = record['skills'].lower().split(', ')
        if skill_name.lower() in skills_list:
            candidates_by_skill.append(record)
    return candidates_by_skill
