import json

def main():
    src = json.load(open("C_1_1_smp_cl_08-27_11-27-00_a_for_DF2.json"))
    # print("breakpoint")

    filename = src["info"]["filename"]
    duration = src["info"]["video_length"]
    activity = src["annotations"][0]["class_name"]
    time = src["info"]["time"]
    location = src["info"]["location"]
    person_present = "unknown"
    source = "AI Hub Dataset"
    sentences_kor = src["events"][0]["class_description"]    
    sentences_eng = []  # TODO: translate sentences_kor to sentences_eng
    words_per_sentence = []
    for sentence in sentences_eng:
        words_per_sentence.append(len(sentence.split()))
    total_sentences = len(sentences)
    
    print("breakpoint")

    ''' HACK: dst format
    "videos": [
      {
        "filename": "tour0001.mp4",
        "duration": "00:05:32",
        "activity" : "hiking",
        "time" : "day",
        "location": "outdoor",
        "person_present": "y",
        "source": "출처",
        "sentences": [
          "영상1의 문장1",
          "영상1의 문장2",
          "영상1의 문장3",
          "영상1의 문장4",
          "영상1의 문장5"
        ],
        "words_per_sentence": [
          6,
          8,
          7,
          5,
          9
        ],
        "total_sentences": 5
      }
    '''

if __name__=="__main__":
    main()