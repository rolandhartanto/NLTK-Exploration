from nltk.chat.util import Chat, reflections
pairs = [
    [
        r'(hi|halo)',
        ['halo']
    ],
    [
        r'(nama saya) (.*)',
        ['Hi %2']
    ],
    [
        r'(.*)hobi[^ku](.*)',
        ['Hobiku menonton film']
    ],
    [
        r'(.*)suka film apa\?',
        ['Avengers Infinity War adalah film favoritku :D']
    ],
    [
        r'(.*)suka film[^apa](.*)',
        ['Saya juga suka film %2','Saya tidak bisa melupakan film %2']
    ],
    [
        r'Lawan kata (.*)', 
        [
            '%1'
        ],
    ],
    [
        r'(.*)', 
        [
            'maaf saya tidak mengerti :D',
            'saya masih harus belajar bahasa manusia lebih banyak'
        ],
    ]
]

reflections = {
    'kamu' : 'aku',
    'kecil' : 'besar',
    'pendek' : 'panjang',
    'rendah' : 'tinggi',
    'awal' : 'akhir',
    'banyak' : 'sedikit',
    'dingin' : 'panas',
    'hulu' : 'hilir',
    'genap' : 'ganjil',
    'ingat' : 'lupa',
    'renggang' : 'erat',
    'ya' : 'tidak',
    'turun' : 'naik',
    'kering' : 'basah',
    'rajin' : 'malas',
    'baik' : 'buruk',
    'baru' : 'tua',
    'benar' : 'salah',
    'mudah' : 'sulit',

    'aku' : 'kamu',
    'besar' : 'kecil',
    'panjang' : 'pendek',
    'tinggi' : 'rendah',
    'akhir' : 'awal',
    'sedikit' : 'banyak',
    'panas' : 'dingin',
    'hilir' : 'hulu',
    'ganjil' : 'genap',
    'lupa' : 'ingat',
    'renggang' : 'erat',
    'tidak' : 'ya',
    'naik' : 'turun',
    'basah' : 'kering',
    'malas' : 'rajin',
    'buruk' : 'baik',
    'tua' : 'baru',
    'salah' : 'benar',
    'sulit' : 'mudah',
}

def chatbot_test():
    print("Selamat datang! Nama saya Chatindo. Chat bot yang sedang belajar bahasa manusia")
    print("Siapa namamu?")
    chat = Chat(pairs, reflections)
    chat.converse()
    
if __name__ == "__main__":
    chatbot_test()