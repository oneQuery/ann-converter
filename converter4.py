import json
from googletrans import Translator

def main():
    ### Parse source json file
    src = json.load(open("C_1_1_smp_cl_08-27_11-27-00_a_for_DF2.json"))

    filename = src["info"]["filename"]
    duration = src["info"]["video_length"]
    activity = src["annotations"][0]["class_name"]
    time = src["info"]["time"]
    location = src["info"]["location"]
    person_present = "unknown"
    source = "AI Hub Dataset"
    
    sentences_kor = []
    sentences_kor.append(src["events"][0]["class_description"])
    # TODO: Other korean sentences
    
    translator = Translator()
    sentences_eng = []
    for sentence_kor in sentences_kor:
      sentence_eng = translator.translate(sentence_kor, dest='en').text
      sentences_eng.append(sentence_eng)
     
    words_per_sentence = []
    for sentence in sentences_eng:
        words_per_sentence.append(len(sentence.split()))
    
    total_sentences = len(sentences_eng)
    
    ### Create target json file
    trg = {}
    
    trg['videos'] = []
    trg['videos'].append({
        'filename': filename,
        'duration': duration,
        'activity': activity,
        'time': time,
        'location': location,
        'person_present': person_present,
        'source': source,
        'sentences_kor': sentences_kor,
        'sentences_eng': sentences_eng,
        'words_per_sentence': words_per_sentence,
        'total_sentences': total_sentences
    })
    
    with open('target.json', 'w') as outfile:
        json.dump(trg, outfile, ensure_ascii=False, indent=4)

if __name__=="__main__":
    main()