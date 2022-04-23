from flask import Flask, render_template, request
from utils import load_candidates_from_json, get_candidate, get_candidates_by_age, get_candidates_by_skills


app = Flask(__name__)
candidates = load_candidates_from_json()

@app.route('/')
def main_route():
    return render_template("list.html", items=candidates)


@app.route('/candidate/<int:candidate_id>')
def candidate_route(candidate_id):
    candidate = get_candidate(candidates, candidate_id)
    return  render_template("single.html", candidate=candidate)


@app.route('/search/<int:candidate_age>')
def candidates_by_age_route(candidate_age):
    candidates_by_age = get_candidates_by_age(candidates, candidate_age)
    candidates_quantity = len(candidates_by_age)
    return  render_template("search.html", candidates=candidates_by_age, candidates_quantity=candidates_quantity)


@app.route('/skill/<skill_name>')
def candidates_by_skills_route(skill_name):
    candidates_by_skill = get_candidates_by_skills(candidates, skill_name)
    candidates_quantity = len(candidates_by_skill)
    return render_template("skill.html", candidates=candidates_by_skill,
                           skill=skill_name, candidates_quantity=candidates_quantity)


app.run()
