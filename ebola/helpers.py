import collections
from phonenumbers import parse as parse_number, format_number, is_possible_number, PhoneNumberFormat
from collections import OrderedDict

payment_type = OrderedDict([
    ('salary',  'Basic salary'),
    ('allowance',  'General allowance'),
    ('hazard',  'Hazard or response pay'),
    # ('response',  'Response pay'),
    ('risk', 'Death benefit'),
    # ('unknown',  'Unsure'),
    ('other', 'Other')
])

payment_type_color = {
    'salary': 'b44d54',
    'hazard': '68acba',
    'allowance': '7c5866',
    # 'response': 'e3bb56',
    'risk': 'e3bb56',
    # 'unknown': 'a88648',
    'other': 'a88648'
}

payment_issue = OrderedDict([
    ('not_paid',  'Not paid'),
    ('delayed',  'Delayed payment'),
    ('incorrect',  'Incorrect payment amount'),
    ('other',  'Other')
])

workplace = OrderedDict([
    ('etu', 'ETU'),
    ('response', 'Response Teams'),
    ('hospital', 'Hospital'),
    ('moh', 'Ministry of Health')
])

organization_type = OrderedDict([
    ('moh',  'Ministry of Health'),
    ('ingo',  'International NGO'),
    ('lngo',  'Liberian NGO'),
    ('clinic',  'Private Clinic'),
    ('other',  'Other')
])

status = OrderedDict([
    ('pending',  'Pending'),
    ('open',  'Open'),
    ('resolved',  'Resolved'),
    ('closed',  'Closed'),
    ('duplicate',  'Duplicate'),
    ('deleted',  'Deleted')
])

reason = OrderedDict([
    ('duplicate',  'Repeat caller'),
    ('connection',  'Lost connection'),
    ('noise',  'Could not hear caller'),
    ('prank',  'Prank call'),
    ('abusive',  'Caller was abusive'),
    ('other',  'Other')
])

language = OrderedDict([
    ('bandi',  'Bandi'),
    ('bassa',  'Bassa'),
    ('dan',  'Dan'),
    ('dewoin',  'Dewoin'),
    ('english',  'English'),
    ('gbii',  'Gbii'),
    ('glaro',  'Glaro'),
    ('glio',  'Glio'),
    ('gola',  'Gola'),
    ('grebo',  'Grebo'),
    ('kisi',  'Kisi'),
    ('klao',  'Klao'),
    ('kpelle',  'Kpelle'),
    ('krahn',  'Krahn'),
    ('krumen',  'Krumen'),
    ('kuwaa',  'Kuwaa'),
    ('loma',  'Loma'),
    ('maninka',  'Maninka'),
    ('maninkakan',  'Maninkakan'),
    ('mann',  'Mann'),
    ('manya',  'Manya'),
    ('mende',  'Mende'),
    ('sapo',  'Sapo'),
    ('tajuasohn',  'Tajuasohn'),
    ('vai',  'Vai')
])

county = OrderedDict([
    ('bomi',  'Bomi'),
    ('bong',  'Bong'),
    ('gbarpolu',  'Gbarpolu'),
    ('grand_bassa',  'Grand Bassa'),
    ('grand_cape_mount',  'Grand Cape Mount'),
    ('grand_gedeh',  'Grand Gedeh'),
    ('grand_kru',  'Grand Kru'),
    ('lofa',  'Lofa'),
    ('margibi',  'Margibi'),
    ('maryland',  'Maryland'),
    ('montserrado',  'Montserrado'),
    ('nimba',  'Nimba'),
    ('rivercess',  'Rivercess'),
    ('river_gee',  'River Gee'),
    ('sinoe',  'Sinoe')
])

sex = OrderedDict([
    ('m',  'Male'),
    ('male',  'Male'),
    ('f',  'Female'),
    ('female',  'Female')
])

suffix = OrderedDict([
    ('',  ''),
    ('jf',  'Jr.'),
    ('sr',  'Sr.'),
    ('ii',  'II'),
    ('iii',  'III')
])

yes_no = OrderedDict([
    ('y',  'Yes'),
    ('yes',  'Yes'),
    (True,  'Yes'),
    ('n',  'No'),
    ('no',  'No'),
    (False,  'No')
])

COUNTRY_CODE = 'LR'


def nesteddict():
    return collections.defaultdict(nesteddict)


def e164_phone_number(phone_number):
    number = parse_number(phone_number, COUNTRY_CODE)
    if is_possible_number(number):
        return str(format_number(number, PhoneNumberFormat.E164)).replace(" ", "")


def local_phone_number(phone_number):
    number = parse_number(phone_number, COUNTRY_CODE)
    if is_possible_number(number):
        return str(format_number(number, PhoneNumberFormat.NATIONAL)).replace(" ", "")


def international_phone_number(phone_number):
    number = parse_number(phone_number, COUNTRY_CODE)
    if is_possible_number(number):
        return str(format_number(number, PhoneNumberFormat.INTERNATIONAL)).replace(" ", "")

