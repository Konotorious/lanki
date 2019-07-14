# !python -m spacy download de
import spacy
import argparse

nlp = spacy.load("de")

def dress_brackets(target, prompt, cn):
    
    output = "{{"+"c{}::{}::{}".format(cn, target, prompt)+"}}"
    return output

def post_process(string):
    """
    Formats the output of the main function (removes blanks before commas and periods).
    """
    output = string
    for punct in ':;.,?!¡¿»«"':
        output = output.replace(" "+punct,punct)
    return output

def tagNamer(token):
    
    tag = token.tag_
    lemma = token.lemma_
    
    if tag in ["NNP","NN"]:
        return "n."
    elif tag in ["NNPS","NNS"]:
        return "n., plural"
    elif tag in ["VAPP","VVPP", "VMPP"]:
        return "v., participle"
    elif tag in ["VIMP", "VAIMP"]:
        return "v., imperative"
    elif tag in ["VAFIN", "VAINF","VMFIN","VMINF", "VVFIN", "VVINF"]:
        return "v."
    elif tag in ["ART"]:
        if lemma[0:3] == "ein":
            return "indef.ar."
        elif lemma[0:2] == "de":
            return "def.ar."
        else:
            return lemma
    elif tag in ["PRELAT","PWAT", "PRELS"]:
        return "pr."
    elif tag in ["PDAT","PDS"]:
        return "demonstrative pr."
    elif tag in ["PIS"]:
        return "indef.pr."
    elif tag in ["PPOSAT","PPOSS"]:
        return "poss.pr."
    elif tag in ["PRF"]:
        return "ref.pr."
    elif tag in ["PIAT","PIDAT"]:
        return "dr."
    elif tag in ["ADJA"]:
        return "adj."
    elif tag in ["ADJD", "ADV"]:
        return "adj./adv."
    else:
        return tag+", "+spacy.explain(tag)
    

def clozer(f):

    doc = nlp(f)
    incPos = ['VERB', 'NOUN', 'PRON','ADJ', 'DET', "AUX"]
    excTag = ["PPER"]

    for sent in doc.sents:
        cn = 1
        consecutive = 0
        output = []
        for i, token in enumerate(sent):
            if not token.is_alpha:
                output.append(token.text)
                continue
            if (token.pos_ in incPos) and (token.tag_ not in excTag):
                #clozed_token_text = dress_brackets(token.text, token.pos_+", "+token.lemma_,cn)
                if not token.pos_ in ["DET","PRON"]:
                    clozed_token_text = dress_brackets(token.text, tagNamer(token)+", "+token.lemma_,cn)
                else:
                    clozed_token_text = dress_brackets(token.text, tagNamer(token),cn)
                output.append(clozed_token_text)
                consecutive = 1
            else:
                output.append(token.text)
                #if token.pos_ not in ["ADP"]:
                if (token.tag_ not in ["APPRART"]) or (token.dep_ not in ["sb"]):
                    cn += consecutive
                    consecutive = 0
        output = ' '.join(output)
        
        yield(post_process(output))

def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs="*")
    args = parser.parse_args()
    output_f = args.files[0]
    input_fs = args.files[1:]

    outF = open(output_f, "w")
    for input_f in input_fs:
        inF = open(input_f, "r")
        cloze_sentences = clozer(inF.read())
        for sentence in cloze_sentences:
            outF.write(sentence)
            outF.write('\n')
        inF.close()
    outF.close()



if __name__ == "__main__":
    main()
