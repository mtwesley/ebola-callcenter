import collections

def nesteddict():
    return collections.defaultdict(nesteddict)

call_type = {
    'case_report': 'New Case Report',
    'case_update': 'Case Report Update',
    'case_inquiry': 'Case Inquiry',
    'general_inquiry': 'General Inquiry'
}

relationship = {
    'spouse': 'Spouse',
    'parent': 'Parent',
    'child': 'Child',
    'relative': 'Other relative',
    'non_relative': 'Other non-relative'
}

condition = {
    'alive': 'Alive',
    'conscious': 'Conscious',
    'unconscious': 'Unconscious',
    'dead': 'Dead'
}

reason = {
    'connection': 'Lost connection',
    'noise': 'Cound not hear caller',
    'prank': 'Prank call',
    'abusive': 'Caller was abusive',
    'other': 'Other'
}

language = {
    'bandi': 'Bandi',
    'bassa': 'Bassa',
    'dan': 'Dan',
    'dewoin': 'Dewoin',
    'english': 'English',
    'gbii': 'Gbii',
    'glaro': 'Glaro',
    'glio': 'Glio',
    'gola': 'Gola',
    'grebo': 'Grebo',
    'kisi': 'Kisi',
    'klao': 'Klao',
    'kpelle': 'Kpelle',
    'krahn': 'Krahn',
    'krumen': 'Krumen',
    'kuwaa': 'Kuwaa',
    'loma': 'Loma',
    'maninka': 'Maninka',
    'maninkakan': 'Maninkakan',
    'mann': 'Mann',
    'manya': 'Manya',
    'mende': 'Mende',
    'sapo': 'Sapo',
    'tajuasohn': 'Tajuasohn',
    'vai': 'Vai'
}

county = {
    None: None,
    '': '',
    'bomi': 'Bomi',
    'bong': 'Bong',
    'gbarpolu': 'Gbarpolu',
    'grand_bassa': 'Grand Bassa',
    'grand_cape_mount': 'Grand Cape Mount',
    'grand_gedeh': 'Grand Gedeh',
    'grand_kru': 'Grand Kru',
    'lofa': 'Lofa',
    'margibi': 'Margibi',
    'maryland': 'Maryland',
    'montserrado': 'Montserrado',
    'nimba': 'Nimba',
    'rivercess': 'Rivercess',
    'river_gee': 'River Gee',
    'sinoe': 'Sinoe'
}

symptom = {
    None: None,
    '': '',
    'abdominal_pain': 'Abdominal Pain',
    'black_stool': 'Black Stool',
    'diarrhea': 'Diarrhea',
    'difficulty_breathing': 'Difficulty Breathing',
    'difficulty_swallowing': 'Difficulty Swallowing',
    'fever': 'Fever',
    'headache': 'Headache',
    'hiccups': 'Hiccups',
    'loss_of_appetite': 'Loss of Appetite',
    'muscle_pain': 'Muscle Pain',
    'nausea': 'Nausea',
    'red_eyes': 'Red Eyes',
    'skin_rash': 'Skin Rash',
    'sore_throat': 'Sore Throat',
    'unexplained_bleeding': 'Unexplained Bleeding',
    'vomiting': 'Vomiting',
    'weakness': 'Weakness'
}

sex = {
    'm': 'Male',
    'male': 'Male',
    'f': 'Female',
    'female': 'Female'
}

suffix = {
    '': '',
    'jf': 'Jr.',
    'sr': 'Sr.',
    'ii': 'II',
    'iii': 'III'
}

yes_no = {
    'y': 'Yes',
    'yes': 'Yes',
    True: 'Yes',
    'n': 'No',
    'no': 'No',
    False: 'No'
}

