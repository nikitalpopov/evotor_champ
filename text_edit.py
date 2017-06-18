import csv
import pymorphy2
from pandas import read_csv


def clean_text(csv_input_file):
    train = read_csv(csv_input_file, encoding='utf-8')

    # All text to lower case
    train.NAME = train.NAME.str.lower()
    train.NAME = ' ' + train.NAME + ' '

    # Cleaning text from useless characters
    train.NAME = train.NAME.str.replace(r'[^\u0400-\u04FFa-zA-Z]', u' ')
    train.NAME = train.NAME.str.replace(' л ', ' литр ')
    train.NAME = train.NAME.str.replace(' мл ', ' миллилитр ')
    train.NAME = train.NAME.str.replace(' г ', ' грамм ')
    train.NAME = train.NAME.str.replace(' гр ', ' грамм ')
    train.NAME = train.NAME.str.replace(' кг ', ' килограмм ')
    train.NAME = train.NAME.str.replace(' мг ', ' миллиграмм')
    train.NAME = train.NAME.str.replace(' шт ', ' штук ')
    train.NAME = train.NAME.str.replace(' муж ', ' мужской ')
    train.NAME = train.NAME.str.replace(' мужск ', ' мужской ')
    train.NAME = train.NAME.str.replace(' жен ', ' женский ')
    train.NAME = train.NAME.str.replace(' женск ', ' женский ')
    train.NAME = train.NAME.str.replace(' сиг ', ' сигареты ')
    train.NAME = train.NAME.str.replace(' уп ', ' упаковка ')
    train.NAME = train.NAME.str.replace(' нап ', ' напиток ')
    train.NAME = train.NAME.str.replace(' наб ', ' набор ')
    train.NAME = train.NAME.str.replace(' арт ', ' артикул ')
    train.NAME = train.NAME.str.replace(' жев рез ', ' жевательная резинка ')
    train.NAME = train.NAME.str.replace(' ориг ', ' оригинальный ')
    train.NAME = train.NAME.str.replace(' увлаж ', ' увлажняющий ')
    train.NAME = train.NAME.str.replace(' таб ', ' таблетки ')
    train.NAME = train.NAME.str.replace(' табл ', ' таблетки ')
    train.NAME = train.NAME.str.replace(' сух ', ' сухое ')
    train.NAME = train.NAME.str.replace(' сл ', ' сладкое ')
    train.NAME = train.NAME.str.replace(' ябл ', ' яблоко ')
    train.NAME = train.NAME.str.replace(' синт ', ' синтетический ')
    train.NAME = train.NAME.str.replace(' ассорт ', ' ассортимент ')
    train.NAME = train.NAME.str.replace(' асс ', ' ассортимент ')
    train.NAME = train.NAME.str.replace(' алк ', ' алкоголь ')
    train.NAME = train.NAME.str.replace(' об ', ' оборот ')
    train.NAME = train.NAME.str.replace(' мент ', ' ментол ')
    train.NAME = train.NAME.str.replace(' рул ', ' рулон ')
    train.NAME = train.NAME.str.replace(' бут ', ' бутылка ')
    train.NAME = train.NAME.str.replace(' д ', ' для ')
    train.NAME = train.NAME.str.replace(' барх ', ' бархат ')
    train.NAME = train.NAME.str.replace(' пост ', ' постельное ')
    train.NAME = train.NAME.str.replace(' б а ', ' безалкогольный ')
    train.NAME = train.NAME.str.replace(' балк ', ' безалкогольный ')
    train.NAME = train.NAME.str.replace(' сл ', ' сладкий ')
    train.NAME = train.NAME.str.replace(' слад ', ' сладкий ')
    train.NAME = train.NAME.str.replace(' нач ', ' начинка ')
    train.NAME = train.NAME.str.replace(' вт ', ' ватт ')
    train.NAME = train.NAME.str.replace(' стир ', ' стирка ')
    train.NAME = train.NAME.str.replace(' газ ', ' газированный ')
    train.NAME = train.NAME.str.replace(' с г ', ' среднегазированный ')
    train.NAME = train.NAME.str.replace(' мин ', ' минеральное ')
    train.NAME = train.NAME.str.replace(' конф ', ' конфеты ')
    train.NAME = train.NAME.str.replace(' бел ', ' белый ')
    train.NAME = train.NAME.str.replace(' чер ', ' черный ')
    train.NAME = train.NAME.str.replace(' черн ', ' черный ')
    train.NAME = train.NAME.str.replace(' роз ', ' розовый ')
    train.NAME = train.NAME.str.replace(' сер ', ' серый ')
    train.NAME = train.NAME.str.replace(' желт ', ' желтый ')
    train.NAME = train.NAME.str.replace(' фиол ', ' фиолетовый ')
    train.NAME = train.NAME.str.replace(' кор ', ' коричневый ')
    train.NAME = train.NAME.str.replace(' зол ', ' золотой ')
    train.NAME = train.NAME.str.replace(' син ', ' синий ')
    train.NAME = train.NAME.str.replace(' кр ', ' красный ')
    train.NAME = train.NAME.str.replace(' крас ', ' красный ')
    train.NAME = train.NAME.str.replace(' р ', ' размер ')
    train.NAME = train.NAME.str.replace(' подсв ', ' подсвечник ')
    train.NAME = train.NAME.str.replace(' цв ', ' цветной ')
    train.NAME = train.NAME.str.replace(' м ', ' метр ')
    train.NAME = train.NAME.str.replace(' см ', ' сантиметр ')
    train.NAME = train.NAME.str.replace(' св ', ' светлый ')
    train.NAME = train.NAME.str.replace(' светл ', ' светлый ')
    train.NAME = train.NAME.str.replace(' темн ', ' темный ')
    train.NAME = train.NAME.str.replace(' виногр ', ' виноград ')
    train.NAME = train.NAME.str.replace(' игр ', ' игра ')
    train.NAME = train.NAME.str.replace(' наст ', ' настольный ')
    train.NAME = train.NAME.str.replace(' мал ', ' малый ')
    train.NAME = train.NAME.str.replace(' болш ', ' большой ')
    train.NAME = train.NAME.str.replace(' зим ', ' зимний ')
    train.NAME = train.NAME.str.replace(' зимн ', ' зимний ')
    train.NAME = train.NAME.str.replace(' лет ', ' летний ')
    train.NAME = train.NAME.str.replace(' нат ', ' натуральный ')
    train.NAME = train.NAME.str.replace(' кож ', ' кожа ')
    train.NAME = train.NAME.str.replace(' зам ', ' заменитель ')
    train.NAME = train.NAME.str.replace(' туф ', ' туфли ')
    train.NAME = train.NAME.str.replace(' бот ', ' ботинки ')
    train.NAME = train.NAME.str.replace(' сап ', ' сапоги ')
    train.NAME = train.NAME.str.replace(' конс ', ' консервированный ')
    banned = ['грамм', 'килограмм', 'литр', 'ассортимент', 'артикул', ' миллилитр ', ' миллиграмм', ' штук ',
              ' упаковка ', 'метр', 'сантиметр']
    for word in banned:
        train.NAME = train.NAME.str.replace(word, ' ')
    train.NAME = train.NAME.str.replace(' - ', ' ')
    train.NAME = train.NAME.str.replace('[0-9]', ' ')
    train.NAME = train.NAME.str.replace('- ', ' ')
    train.NAME = train.NAME.str.replace(' -', ' ')
    train.NAME = train.NAME.str.replace(u' . ', ' ')
    train.NAME = train.NAME.str.replace(u'.', ' ')
    train.NAME = train.NAME.str.replace(',', ' ')
    train.NAME = train.NAME.str.replace('!', ' ')
    train.NAME = train.NAME.str.replace('/', ' ')
    train.NAME = train.NAME.str.replace('(', ' ')
    train.NAME = train.NAME.str.replace(')', ' ')
    train.NAME = train.NAME.str.replace(':', ' ')
    train.NAME = train.NAME.str.replace('"', ' ')
    train.NAME = train.NAME.str.replace('«', ' ')
    train.NAME = train.NAME.str.replace('»', ' ')
    train.NAME = train.NAME.str.replace(u' +', ' ')
    train.NAME = train.NAME.str.strip()

    return train


def my_tokenizer(s, morph):
    t = s.split(' ')
    f = ''
    for j in t:
        m = morph.parse(j.replace('.', ''))
        if len(m) != 0:
            wrd = m[0]
            if wrd.tag.POS not in ('NUMR', 'PREP', 'CONJ', 'PRCL', 'INTJ', 'NPRO', 'COMP', 'PRED'):
                f = f + ' ' + str(wrd.normal_form)
    return f


def tokenization(train, csv_train_file):
    out_csv = csv.writer(open(csv_train_file, "w", encoding='utf-8'))
    out_csv.writerow(["id", "GROUP_ID", "NAME"])
    morph = pymorphy2.MorphAnalyzer()
    for i in range(train.shape[0]):
        y = train.iloc[i]['NAME']
        if type(y) == str:
            out_csv.writerow([train.iloc[i]['id'], train.iloc[i]['GROUP_ID'], my_tokenizer(y, morph)])
        else:
            out_csv.writerow([train.iloc[i]['id'], train.iloc[i]['GROUP_ID'], []])


def tokenization_test(test, csv_test_file):
    out_csv = csv.writer(open(csv_test_file, "w", encoding='utf-8'))
    out_csv.writerow(["id", "GROUP_ID", "NAME"])
    morph = pymorphy2.MorphAnalyzer()
    for i in range(test.shape[0]):
        y = test.iloc[i]['NAME']
        if type(y) == str:
            out_csv.writerow([test.iloc[i]['id'], [], my_tokenizer(y, morph)])
        else:
            out_csv.writerow([test.iloc[i]['id'], [], []])


def get_output(result, output_file):
    with open(output_file, mode='w', encoding='utf-8') as output:
        output.write('\n'.join(result))
