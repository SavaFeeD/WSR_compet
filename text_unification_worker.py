import my_cleaning_tools as ts









def text_unification_worker():
    competencies = ts.read_json("tidy_dataset.json")
    competencies_text = {'l': []}
    for competence in competencies:
        all_textx_tokens = []
        tokens_collections = competence['tokens_collection']
        for doc_tokens in tokens_collections:
            all_textx_tokens.extend(doc_tokens['tokens'])

        all_textx_tokens.extend(competence['description_tokens'])
        all_text = ' '.join(all_textx_tokens)
        competencies_text['l'].append(all_text)
    ts.save_json(competencies_text, "competencies_text.json")


def text_description_worker():
    competencies = ts.read_json("tidy_dataset.json")
    competencies_text = {'l': []}
    for competence in competencies:
        all_textx_tokens = []
        all_textx_tokens.extend(competence['description_tokens'])
        all_text = ' '.join(all_textx_tokens)
        competencies_text['l'].append(all_text)
    ts.save_json(competencies_text, "competencies_descriptions_text.json")




def text_sections_unification_worker():
    competencies = ts.read_json("tidy_dataset.json")
    competencies_text = {'l': []}
    for competence in competencies:
        all_textx_tokens = []
        tokens_collections = competence['tokens_collection']
        for doc_tokens in tokens_collections:
            all_textx_tokens.extend(doc_tokens['tokens'])

        all_text = ' '.join(all_textx_tokens)
        competencies_text['l'].append(all_text)
    ts.save_json(competencies_text, "sections_competencies_text.json")



def skills_titles_unification_worker():
    competencies = ts.read_json('tidy_dataset.json')
    all_titles_tokens = []
    for competence in competencies:
        competence_specification = competence['competence_specification']
        titles_tokens = []
        sections = competence_specification['sections']
        for section in sections:
            tokens = []
            section_rate = int(section['section_rate'] * 100)
            section_title = section['section_title']
            cleaned_tokens, cleaned_title = ts.total_cleaner(section_title)
            for i in range(section_rate):
                tokens.extend(cleaned_tokens)
            titles_tokens.extend(tokens)
        all_titles_tokens.append(' '.join(titles_tokens))

    ts.save_json(all_titles_tokens, "all_titles_tokens.json")
    return all_titles_tokens





def main():
    # text_sections_unification_worker()
    skills_titles_unification_worker()


if __name__ == "__main__":
    main()


