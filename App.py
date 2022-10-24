import streamlit as st
from PIL import Image
import json
from Classifier import KNearestNeighbours
from bs4 import BeautifulSoup
import requests,io
import PIL.Image
from urllib.request import urlopen

with open('./Data/book_data.json', 'r+', encoding='utf-8') as f:
    data = json.load(f)
with open('./Data/book_title.json', 'r+', encoding='utf-8') as f:
    book_title = json.load(f)

def book_poster_fetcher(book_link):
    url_data = requests.get(book_link).text
    s_data = BeautifulSoup(url_data, 'html.parser')
    rate_dp = s_data.find("meta", property="og:image")
    book_poster_link = rate_dp.attrs['content']
    u = urlopen(book_poster_link)
    raw_data = u.read()
    image = PIL.Image.open(io.BytesIO(raw_data))
    image = image.resize((301, 301), )
    st.image(image, use_column_width=False)


def KNN_Book_Recommender(test_point, k):
    target = [0 for item in book_title]
    model = KNearestNeighbours(data, target, test_point, k=k)
    model.fit()
    table = []
    for i in model.indices:
        table.append([book_title[i][0], book_title[i][2],data[i][-1]])
    print(table)
    return table

st.set_page_config(
   page_title="Book Recommendation System",
)

def run():
    img1 = Image.open('./meta/logos.jpg')
    img1 = img1.resize((700,250),)
    st.image(img1,use_column_width=False)
    st.title("Book Recommendation System")
    st.markdown('''<h4 style='text-align: left; color: #d73b5c;'></h4>''',
                unsafe_allow_html=True)
    genres = ['12th Century','14th Century','15th Century','16th Century','17th Century','18th Century', '19th Century', '1st Grade',
    '20th Century','21st Century','40k','Abuse', 'Academia', 'Academic', 'Action', 'Activism', 'Adoption', 'Adult', 'Adult Fiction',
    'Adventure','Aeroplanes','Africa','African American','African American Literature','African Literature','Agriculture','Albanian Literature',
    'Alchemy','Alcohol','Algeria','Aliens','Alternate History','Alternate Universe','Amateur Sleuth','Amazon','American','American Civil War',
    'American Fiction','American History','American Revolution','American Revolutionary War','Americana','Amish','Amish Fiction','Anarchism',
    'Ancient', 'Ancient History', 'Angels', 'Anglo Saxon', 'Angola', 'Animal Fiction', 'Animals', 'Anime', 'Anthologies', 'Anthropology',
    'Anthropomorphic', 'Anti Racist', 'Apocalyptic', 'Apple', 'Archaeology', 'Architecture', 'Art', 'Art Design', 'Art History', 'Art and Photography',
    'Arthurian','Artificial Intelligence', 'Asia', 'Asian Literature', 'Aspergers', 'Astronomy','Atheism','Audiobook','Australia','Autistic Spectrum Disorder',
    'Autistic Spectrum...','Autobiography','Aviation','BDSM','Bande Dessinée','Bangladesh','Banking','Banks','Banned Books','Baseball','Basketball','Batman',
    'Beauty and The Beast','Belgian', 'Belgium', 'Biblical', 'Biblical Fiction', 'Biography', 'Biography Memoir', 'Biology' 'Birds',
    'Bisexual','Bizarro Fiction','Boarding School','Bolivia','Book Club','Books About Books','Botswana','Brain','Brazil','British Literature',
    'Buddhism','Buisness','Bulgaria',
    'Business',
    'Canada',
    'Canadian Literature',
    'Cars',
    'Cartography',
    'Catholic',
    'Cats',
    'Central Africa',
    'Chapter Books',
    'Chemistry',
    'Chick Lit',
    'Childrens',
    'China',
    'Chinese Literature',
    'Christian',
    'Christian Fantasy',
    'Christian Fiction',
    'Christian Historical Fiction',
    'Christian Living',
    'Christian Non Fiction',
    'Christian Romance',
    'Christianity',
    'Christmas',
    'Church',
    'Church History',
    'Church Ministry',
    'Cinderella',
    'Cities',
    'Civil War',
    'Class',
    'Classical Music',
    'Classics',
    'Clean Romance',
    'Climate Change',
    'Climate Change Fiction',
    'Climbing',
    'Coding',
    'Collections',
    'College',
    'Combat',
    'Comedian',
    'Comedy',
    'Comic Book',
    'Comic Fantasy',
    'Comic Strips',
    'Comics',
    'Comics Bd',
    'Comics Manga',
    'Coming Of Age',
    'Comix',
    'Communication',
    'Computer Science',
    'Computers',
    'Conservation',
    'Conspiracy Theories',
    'Contemporary',
    'Contemporary Romance',
    'Cookbooks',
    'Cooking',
    'Counselling',
    'Counter Culture',
    'Counting',
    'Couture',
    'Cozy Mystery',
    'Crafts',
    'Crime',
    'Criticism',
    'Cuisine',
    'Culinary',
    'Cult Classics',
    'Cults',
    'Cultural',
    'Cultural Studies',
    'Culture',
    'Currency',
    'Cyberpunk',
    'Cycling',
    'Czech Literature',
    'Danish',
    'Dark',
    'Dark Fantasy',
    'Dc Comics',
    'Death',
    'Demons',
    'Denmark',
    'Design',
    'Detective',
    'Diary',
    'Dictionaries',
    'Diets',
    'Dinosaurs',
    'Disability',
    'Discipleship',
    'Disease',
    'Divorce',
    'Doctor Who',
    'Doctors',
    'Dogs',
    'Dragons',
    'Drama',
    'Drawing',
    'Dungeons and Dragons',
    'Dutch Literature',
    'Dystopia',
    'Earth',
    'Earth Sciences',
    'Eastern Africa',
    'Ecclesiology',
    'Ecology',
    'Economics',
    'Education',
    'Edwardian',
    'Egypt',
    'Egyptian Literature',
    'Elizabethan Period',
    'Elves',
    'Emergency Services',
    'Emotion',
    'Engineering',
    'English History',
    'Entrepreneurship',
    'Environment',
    'Epic',
    'Epic Fantasy',
    'Erotic Romance',
    'Erotica',
    'Esoterica',
    'Espionage',
    'Essays',
    'Ethiopia',
    'European History',
    'European Literature',
    'Evangelism',
    'Evolution',
    'Experimental Archaeology',
    'Fables',
    'Fae',
    'Fairies',
    'Fairy Tale Retellings',
    'Fairy Tales',
    'Faith',
    'Family',
    'Family Law',
    'Fan Fiction',
    'Fandom',
    'Fantasy',
    'Fantasy Of Manners',
    'Fantasy Romance',
    'Fashion',
    'Favorites',
    'Female Authors',
    'Feminism',
    'Feminist Theory',
    'Fiction',
    'Fighters',
    'Film',
    'Finance',
    'Finnish Literature',
    'Fitness',
    'Folk Tales',
    'Folklore',
    'Food',
    'Food History',
    'Food Writing',
    'Food and Drink',
    'Food and Wine',
    'Foodie',
    'Football',
    'Forgotten Realms',
    'Fostering',
    'France',
    'French Literature',
    'French Revolution',
    'Futurism',
    'Futuristic',
    'GLBT',
    'Game Design',
    'Games',
    'Gaming',
    'Gardening',
    'Gastronomy',
    'Gay',
    'Gay Fiction',
    'Gay For You',
    'Gay Romance',
    'Geek',
    'Gender',
    'Gender Studies',
    'Gender and Sexuality',
    'Genetics',
    'Geography',
    'Geology',
    'Georgian',
    'German Literature',
    'Germany',
    'Ghana',
    'Ghost Stories',
    'Ghosts',
    'Gnosticism',
    'Gods',
    'Google',
    'Goth',
    'Gothic',
    'Government',
    'Grad School',
    'Graphic Novels',
    'Graphic Novels Comics',
    'Graphic Novels Comics Manga',
    'Graphic Novels Manga',
    'Greece',
    'Greek Mythology',
    'Green',
    'Guides',
    'Halloween',
    'Hard Science Fiction',
    'Harem',
    'Harlequin',
    'Health',
    'Health Care',
    'Heroic Fantasy',
    'High Fantasy',
    'High School',
    'Hip Hop',
    'Historical',
    'Historical Fantasy',
    'Historical Fiction',
    'Historical Mystery',
    'Historical Romance',
    'History',
    'History Of Science',
    'Holiday',
    'Holocaust',
    'Horror',
    'Horse Racing',
    'Horses',
    'Horticulture',
    'How To',
    'Hqn',
    'Hugo Awards',
    'Human Resources',
    'Humanities',
    'Humor',
    'Hungarian Literature',
    'Hungary',
    'Illness',
    'India',
    'Indian Literature',
    'Indonesian Literature',
    'Inspirational',
    'Intelligent Design',
    'International',
    'International Development',
    'International Literature',
    'International Rel...',
    'International Relations',
    'Internet',
    'Interracial Romance',
    'Iran',
    'Ireland',
    'Irish Literature',
    'Islam',
    'Israel',
    'Italian Literature',
    'Italy',
    'Japan',
    'Japanese Literature',
    'Jazz',
    'Jewish',
    'Journal',
    'Journaling',
    'Journalism',
    'Judaica',
    'Judaism',
    'Juvenile',
    'Kenya',
    'Kids',
    'Knitting',
    'LGBT',
    'Labor',
    'Language',
    'Latin American',
    'Latin American Literature',
    'Law',
    'Lds',
    'Lds Fiction',
    'Leadership',
    'Lebanon',
    'Legal Thriller',
    'Lesbian',
    'Lesbian Fiction',
    'Librarianship',
    'Library Science',
    'Light Novel',
    'Linguistics',
    'Lit Crit',
    'Literary Criticism',
    'Literary Fiction',
    'Literature',
    'Logic',
    'Love',
    'Love Story',
    'Lovecraftian',
    'Low Fantasy',
    'M F M',
    'M F Romance',
    'M M Contemporary',
    'M M F',
    'M M Fantasy',
    'M M Historical Romance',
    'M M M',
    'M M Romance',
    'Magic',
    'Magical Realism',
    'Malawi',
    'Management',
    'Managers',
    'Manga',
    'Maps',
    'Marathi',
    'Maritime',
    'Marriage',
    'Martial Arts',
    'Marvel',
    'Mathematics',
    'Media Tie In',
    'Medical',
    'Medicine',
    'Medieval',
    'Medieval History',
    'Medieval Romance',
    'Medievalism',
    'Memoir',
    'Menage',
    'Mental Health',
    'Mental Illness',
    'Mermaids',
    'Metaphysics',
    'Microhistory',
    'Middle Grade',
    'Military',
    'Military Fiction',
    'Military History',
    'Military Romance',
    'Military Science Fiction',
    'Mine',
    'Modern',
    'Modern Classics',
    'Money',
    'Monsters',
    'Mormonism',
    'Morocco',
    'Moscow',
    'Motorcycle',
    'Mountaineering',
    'Murder Mystery',
    'Music',
    'Music Biography',
    'Musicals',
    'Musicians',
    'Muslimah',
    'Muslims',
    'Mystery',
    'Mystery Thriller',
    'Mythology',
    'Namibia',
    'Native American History',
    'Native Americans',
    'Natural History',
    'Nature',
    'Naval History',
    'Near Future',
    'Neurodiversity',
    'Neuroscience',
    'New Adult',
    'New Age',
    'New Testament',
    'New Weird',
    'New York',
    'Nigeria',
    'Nobel Prize',
    'Noir',
    'Nonfiction',
    'Nordic Noir',
    'North American Hi...',
    'Northern Africa',
    'Novella',
    'Novels',
    'Number',
    'Nursery Rhymes',
    'Nurses',
    'Nursing',
    'Nutrition',
    'Occult',
    'Old Testament',
    'Omegaverse',
    'Oral History',
    'Ornithology',
    'Outdoors',
    'Own',
    'Paganism',
    'Pakistan',
    'Palaeontology',
    'Paranormal',
    'Paranormal Mystery',
    'Paranormal Romance',
    'Parenting',
    'Personal Development',
    'Personal Finance',
    'Philosophy',
    'Photography',
    'Physics',
    'Picture Books',
    'Pirates',
    'Plantagenet',
    'Plants',
    'Plays',
    'Poetry',
    'Poetry Plays',
    'Poland',
    'Police',
    'Polish Literature',
    'Political Science',
    'Politics',
    'Polyamorous',
    'Polyamory',
    'Polygamy',
    'Pop Culture',
    'Popular Science',
    'Pornography',
    'Portugal',
    'Portuguese Literature',
    'Post Apocalyptic',
    'Post Colonial',
    'Poverty',
    'Prayer',
    'Pre K',
    'Prehistoric',
    'Presidents',
    'Productivity',
    'Programming',
    'Prostitution',
    'Pseudoscience',
    'Psychiatry',
    'Psychoanalysis',
    'Psychological Thriller',
    'Psychology',
    'Punk',
    'Puzzles',
    'Quantum Mechanics',
    'Queer',
    'Queer Lit',
    'Queer Studies',
    'Quilting',
    'Race',
    'Racing',
    'Railways',
    'Read For School',
    'Realistic Fiction',
    'Recreation',
    'Recruitment',
    'Reference',
    'Regency',
    'Regency Romance',
    'Relationships',
    'Religion',
    'Reportage',
    'Research',
    'Retellings',
    'Reverse Harem',
    'Road Trip',
    'Robots',
    'Rock N Roll',
    'Role Playing Games',
    'Roman',
    'Roman Britain',
    'Romance',
    'Romania',
    'Romanian Literature',
    'Romanovs',
    'Romantic Suspense',
    'Romanticism',
    'Russia',
    'Russian History',
    'Russian Literature',
    'Russian Revolution',
    'Rwanda',
    'Scandinavian Lite...',
    'Scandinavian Literature',
    'School',
    'School Stories',
    'Sci Fi Fantasy',
    'Science',
    'Science Fiction',
    'Science Fiction Fantasy',
    'Science Fiction Romance',
    'Science Nature',
    'Scotland',
    'Scripture',
    'Seinen',
    'Self Help',
    'Senegal',
    'Sequential Art',
    'Sewing',
    'Sex Work',
    'Sexuality',
    'Shapeshifters',
    'Shojo',
    'Shonen',
    'Short Stories',
    'Short Story Collection',
    'Sierra Leone',
    'Singularity',
    'Skepticism',
    'Slice Of Life',
    'Soccer',
    'Social',
    'Social Issues',
    'Social Justice',
    'Social Media',
    'Social Movements',
    'Social Science',
    'Social Work',
    'Society',
    'Sociology',
    'Software',
    'Somalia',
    'South Africa',
    'Southern',
    'Southern Africa',
    'Southern Gothic',
    'Soviet History',
    'Soviet Union',
    'Space',
    'Space Opera',
    'Spain',
    'Spanish Civil War',
    'Spanish Literature',
    'Speculative Fiction',
    'Spirituality',
    'Sports',
    'Sports Romance',
    'Sports and Games',
    'Spy Thriller',
    'Star Trek',
    'Star Wars',
    'Steampunk',
    'Storytime',
    'Sudan',
    'Superheroes',
    'Superman',
    'Supernatural',
    'Surreal',
    'Survival',
    'Suspense',
    'Sustainability',
    'Sweden',
    'Swedish Literature',
    'Sword and Sorcery',
    'Tanzania',
    'Taoism',
    'Tasmania',
    'Teaching',
    'Technical',
    'Technology',
    'Teen',
    'Terrorism',
    'Textbooks',
    'The United States Of America',
    'The World',
    'Theatre',
    'Theology',
    'Theory',
    'Thriller',
    'Time Travel',
    'Time Travel Romance',
    'Tragedy',
    'Trains',
    'Transgender',
    'Transport',
    'Travel',
    'Travelogue',
    'Trivia',
    'True Crime',
    'True Story',
    'Tudor Period',
    'Tunisia',
    'Turkish',
    'Turkish Literature',
    'Tv',
    'Uganda',
    'Ukraine',
    'Ukrainian Literature',
    'Unfinished',
    'Unicorns',
    'United States',
    'Urban',
    'Urban Fantasy',
    'Urban Planning',
    'Urban Studies',
    'Urbanism',
    'Us Presidents',
    'Usability',
    'Utopia',
    'Vampires',
    'Vegan',
    'Vegetarian',
    'Vegetarianism',
    'Victor Frankenstein',
    'Victorian',
    'Video Games',
    'Virtual Reality',
    'Walking',
    'War',
    'Warfare',
    'Web',
    'Webcomic',
    'Weird Fiction',
    'Werewolves',
    'Western Africa',
    'Western Historical Romance',
    'Western Romance',
    'Westerns',
    'Wicca',
    'Wilderness',
    'Wildlife',
    'Wine',
    'Witchcraft',
    'Witches',
    'Wolves',
    'Womens',
    'Womens Fiction',
    'Womens Studies',
    'Wonder Woman',
    'World History',
    'World War I',
    'World War II',
    'Writing',
    'X Men',
    'Yaoi',
    'Young Adult',
    'Young Adult Contemporary',
    'Young Adult Fantasy',
    'Young Adult Historical Fiction',
    'Young Adult Paranormal',
    'Young Adult Romance',
    'Young Adult Science Fiction',
    'Young Readers',
    'Zambia',
    'Zen',
    'Zimbabwe',
    'Zombies',
    'nan']
    books = [title[0] for title in book_title]
    category = ['--Select--', 'Book based', 'Genre based']
    cat_op = st.selectbox('Select Recommendation Type', category)
    if cat_op == category[0]:
        st.warning('Please select Recommendation Type!!')
    elif cat_op == category[1]:
        select_book = st.selectbox('Select Book: (Recommendation will be based on this selection)', ['--Select--'] + books)
        dec = st.radio("Want to Fetch Book Image?", ('Yes', 'No'))
        st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Fetching Images will take a time."</h4>''',
                    unsafe_allow_html=True)
        if dec == 'No':
            if select_book == '--Select--':
                st.warning('Please select Book!!')
            else:
                no_of_reco = st.slider('Number of book you want Recommended:', min_value=5, max_value=20, step=1)
                genres = data[books.index(select_book)]
                test_points = genres
                table = KNN_Book_Recommender(test_points, no_of_reco+1)
                table.pop(0)
                c = 0
                st.success('Some of the books from our Recommendation, have a look below')
                for book, link, ratings in table:
                    c+=1
                    st.markdown(f"({c})[ {book}]({link})")
                    st.markdown('Rating: ' + str(ratings) + '⭐')
        else:
            if select_book == '--Select--':
                st.warning('Please select book!!')
            else:
                no_of_reco = st.slider('Number of books you want Recommended:', min_value=5, max_value=20, step=1)
                genres = data[books.index(select_book)]
                test_points = genres
                table = KNN_Book_Recommender(test_points, no_of_reco+1)
                table.pop(0)
                c = 0
                st.success('Some of the books from our Recommendation, have a look below')
                for book, link, ratings in table:
                    c += 1
                    st.markdown(f"({c})[ {book}]({link})")
                    book_poster_fetcher(link)
                    st.markdown('Rating: ' + str(ratings) + '⭐')
    elif cat_op == category[2]:
        sel_gen = st.multiselect('Select Genres:', genres)
        dec = st.radio("Want to Fetch Book Image?", ('Yes', 'No'))
        st.markdown('''<h4 style='text-align: left; color: #d73b5c;'>* Fetching a Books Image will take a time."</h4>''',
                    unsafe_allow_html=True)
        if dec == 'No':
            if sel_gen:
                rating = st.slider('Choose rating:', 1, 5, 8)
                no_of_reco = st.number_input('Number of books:', min_value=5, max_value=20, step=1)
                test_point = [1 if genre in sel_gen else 0 for genre in genres]
                test_point.append(rating)
                table = KNN_Book_Recommender(test_point, no_of_reco)
                c = 0
                st.success('Some of the books from our Recommendation, have a look below')
                for book, link, ratings in table:
                    c += 1
                    st.markdown(f"({c})[ {book}]({link})")
                    st.markdown('Rating: ' + str(ratings) + '⭐')
        else:
            if sel_gen:
                rating = st.slider('Choose rating:', 1, 5, 3)
                no_of_reco = st.number_input('Number of books:', min_value=5, max_value=20, step=1)
                test_point = [1 if genre in sel_gen else 0 for genre in genres]
                test_point.append(rating)
                table = KNN_Book_Recommender(test_point, no_of_reco)
                c = 0
                st.success('Some of the book from our Recommendation, have a look below')
                for book, link, ratings in table:
                    c += 1
                    st.markdown(f"({c})[ {book}]({link})")
                    book_poster_fetcher(link)
                    st.markdown('Rating: ' + str(ratings) + '⭐')
run()