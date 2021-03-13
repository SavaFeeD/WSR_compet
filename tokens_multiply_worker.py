import my_cleaning_tools as ts



def tokens_multiplyer(competence):
    multiply_tokens_collection = []
    tokens_collection = competence['tokens_collection']
    c = 0
    for doc_tokens in tokens_collection:
        new_rate = int(doc_tokens['rate']*100)
        tokens = []
        for i in range(new_rate):
            tokens.extend(doc_tokens['tokens'])
        doc_tokens['tokens'] = tokens
        c += 1
        print(c)





def tokens_multiply_worker():
    competencies = ts.read_json("tidy_dataset.json")
    for competence in competencies:
        tokens_multiplyer(competence)
    # print(competencies[0]['tokens_collection'][0]['tokens'])
    ts.save_json(competencies, "tidy_dataset.json")





def main():
    tokens_multiply_worker()



if __name__ == "__main__":
    main()