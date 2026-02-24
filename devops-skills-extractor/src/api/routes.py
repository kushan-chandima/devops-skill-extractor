from flask import Flask, jsonify, request
from src.extractors.skills_extractor import SkillsExtractor

app = Flask(__name__)
skills_extractor = SkillsExtractor()

@app.route('/api/skills', methods=['GET'])
def get_skills():
    try:
        skills_data = skills_extractor.extract_skills()
        return jsonify(skills_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/skills', methods=['POST'])
def add_skills():
    try:
        new_skills = request.json.get('skills')
        if not new_skills:
            return jsonify({"error": "No skills provided"}), 400
        skills_extractor.add_skills(new_skills)
        return jsonify({"message": "Skills added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)