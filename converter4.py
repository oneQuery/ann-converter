import json
import os

from googletrans import Translator


def main():
    
    src_root = "annotations4"
    ann_files = os.listdir(src_root)
    
    trg = {}
    trg['videos'] = []
    
    for ann_file in ann_files:
        ### Parse source json file
        ann_file_path = os.path.join(src_root, ann_file)
    
        src = json.load(open(ann_file_path, "r"))

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

    print("Done!")

if __name__=="__main__":
    main()