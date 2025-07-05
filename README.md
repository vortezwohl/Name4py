# Name4py

Generate names in every language.

## Installation

- From [PyPi](https://pypi.org/project/name4py/)

```
pip install -U name4py
```

- From [Github](https://github.com/vortezwohl/Name4py/releases/tag/0.0.1)

```
pip install git+https://github.com/vortezwohl/Name4py.git
```

## Quick Start

1. Import SDKs

```python
from name4py import NameGenerator, Country, Gender
```

2. Generate names

```python
available_countries = [Country.CAN, Country.CHN, Country.FRA,
                       Country.DEU, Country.IDN, Country.JPN,
                       Country.KOR, Country.PHL, Country.PRT,
                       Country.RUS, Country.VNM, Country.ESP,
                       Country.THA, Country.GBR, Country.USA]


for country in available_countries:
    surname_first = False
    hyphenate = True
    if country in [Country.CHN, Country.JPN, Country.KOR, Country.VNM]:
        surname_first = True
    if country in [Country.CHN, Country.KOR, Country.JPN]:
        hyphenate = False
    print(NameGenerator(country).batch_generate(batch_size=32, gender=Gender.Female, surname_first=surname_first, hyphenate=hyphenate))
```

output:

```
['Marcelle Ryan', 'Dessie Banks', 'Beuve Vannier', 'Sophie Hémond', 'Aja Franco', 'Malvina Péan', 'Samanta Sargent', 'Elenor Mesnard', 'Helene Wooten', 'Colleen Avery', 'Angella Hébert', 'Anastase Devaux', 'Andrée Fleury', 'Elta Pradeau', 'Keyla Griffin', 'Gracie Michon', 'Jaycee Herbert', 'Anahi Chaigneau', 'Edwina Kennedy', 'Denice Esteve', 'Abigaël Ruault', 'Clyda Robinson', 'Edesse Hardin', 'Edwina Sullivan', 'Charolette Kemp', 'Gearldine Camacho', 'Léopolda Richer', 'Hildegarde Maire', 'Nadège Tellier', 'Dalia Pitts', 'Marcia Gras', 'Natacha Robert']
['赖语桐', '吴梦琪', '程若曦', '武雨婷', '夏晓梅', '史云', '北春华', '廖亚男', '张雪芳', '邹晓丽', '韩玲', '袁霞', '康雨涵', '侯丽娟', '熊子怡', '毕雪芳', '北梅', '何娜', '张雨婷', '孙梦瑶', '戴云', '汤雨桐', '杨雨桐', '廖玉梅', '姜晓霞', '蒋静', '崇亚男', '北静', '胡冬梅', '令秀兰', '武晓敏', '唐娟']
['Dalie Latulippe', 'Bérénice Vandal', 'Shanna Harvey', 'Jeanneton Vion', 'Nadège Provencher', 'Georgina Florentin', 'Avigaëlle Hervé', 'Fiacre Cellier', 'Paquita Delmas', 'Placide Grosset', 'Sidonie Bauer', 'Jannick Tardy', 'Tudal Fréchette', 'Maëla Couvreur', 'Climène Hebert', 'Laurida Julien', 'Valérie Bayle', 'Romaine Herve', 'Fideline Liénard', 'Scolastique Veyssière', 'Maëla Monast', 'Isabel Coutu', 'Lambert Salisbury', 'Zélie Besson', 'Nicoletta Saux', 'Ophélie Gomez', 'Bibiane Delorme', 'Anisette Maury', 'Eireen Guimond', 'Cointa Veyret', 'Adeline Privat', 'Anastase Lombard']
['Caja Stocker', 'Josefina Roder', 'Ruby Ochs', 'Marika Kirch', 'Mirela Reinsch', 'Inka Deutschmann', 'Lilja Schirra', 'Franka Franz', 'Bertina Hartl', 'Jeanna Neller', 'Seraphine Klett', 'Jelka Noll', 'Ayana Dose', 'Mariella Barthold', 'Mariam Heil', 'Berta Schenck', 'Jill Kilian', 'Aurora Blank', 'Janna Schwarzkopf', 'Liara Schwabe', 'Otilia Holtz', 'Eva-Maria Heim', 'Christel Krone', 'Agatha Kukla', 'Undine Nauber', 'Valerija Brückmann', 'Aline Hennig', 'Ceylan Singer', 'Clementina Kobler', 'Amelie Triebel', 'Carine Jablonski', 'Marielle Schlimm']
['Maya Yuliyanto', 'Rena Syarifuddin', 'Gadis Tumbelaka', 'April Suroso', 'Mutiara Sapardi', 'Azalia Nirmala', 'Kinanti Mahfud', 'Alessia Aidid', 'Naila Widjaja', 'Marsela Dedi', 'Krisna Waworuntu', 'Helma Sumarmo', 'Lala Senoadji', 'Athalia Rizky', 'Safitri Nirmala', 'Arsyila Suryadinata', 'Ayuni Yuliyanto', 'Hilda Jusman', 'Rania Soleh', 'Azka Kusumo', 'Yanti Sumitro', 'Keisha Adyatmika', 'Elvina Rini', 'Isabella Baderi', 'Ivone Indrawati', 'Nani Widodo', 'Indah Regar', 'Azzura Priyono', 'Septi Ikhsan', 'Maria Erwin', 'Satya Albuchari', 'Rike Azmi']
['福江真理代', '小林莉愛', '芳賀佳菜', '松井貴穂', '石黒聖世', '益田麻里沙', '神田真理沙', '大江理歌栄', '岩永栞穂', '梅村桃歌音', '庄司楓花', '市村愛子', '西村澄子', '桑山莉葉', '長本優歌栄', '中井瑞枝', '浜口光枝', '伊沢乃音', '秋山奈津穂', '藤島理歌代', '平野華恵', '天野萌', '有馬理沙', '西原安寿', '高島由佳莉', '堀内結枝', '岩佐花梨', '中島亜矢佳', '磯部由穂', '河瀬真悠美', '近藤麻実', '長浜亜矢子']
['옹설아', '명길라', '구수정', '설리희', '소세련', '팽수안', '권희순', '뢰성주', '진리윤', '용백합', '선신아', '독원지', '근자민', '반사랑', '후창숙', '태란', '야승지', '도복실', '궁요나', '화새아', '자제니', '독라은', '백이화', '돈명하', '신옥희', '봉문주', '기유주', '성효주', '우향희', '창서리', '송무궁', '장방울']
['Anaís Fabregat', 'Patricia Pastor', 'Roberta Araujo', 'Eunice Tovar', 'Sofía Puno', 'Yadira Leiva', 'Alejandra Rodríguez', 'Miguela Verdú', 'Dina Amador', 'Ricarda Morell', 'Belinda Tormo', 'Olinda Montserrat', 'Idoia Cuenca', 'Nilda Velázquez', 'Prudencia López', 'Narcisa Palomares', 'Eudelia Chua', 'Florentina Aragon', 'Sandra Morante', 'Zoe Astorga', 'Cristina Abaya', 'Asunción Urbina', 'Bernarda Guardiola', 'Milagros Bravo', 'Izaskun Galindo', 'Iratxe Abeleda', 'Dulce Nantes', 'Inés Mercado', 'Rosenda Ong', 'Dominga Merchán', 'Rosario Cabral', 'Yesenia Huerta']
['Kátia Martins', 'Norma Do Vale', 'Katarina Mendonça', 'Nicole Carrara', 'Giovana Belchior', 'Dirce Sobreira', 'Léa Fernando', 'Consuelo Escobar', 'Melanie Estrela', 'Renata Borges', 'Dóris Gurgel', 'Franca Miranda', 'Amanda Ramires', 'Ofélia De Carvalho', 'Dejanira Villas', 'Noélia Vaz', 'Fabiana Pedrosa', 'Emanuele Amaral', 'Zilda Resende', 'Melina Magalhães', 'Amélia De Góis', 'Janaína Tinoco', 'Sara Villar', 'Alexandra Lousada', 'Léa Alvares', 'Alda Dantas', 'Perpétua Neves', 'Marise Sardinha', 'Dúlcia Guimarães', 'Anaí Bernardino', 'Cloe Caires', 'Verónica Mata']
['Сильва Ахматов', 'Рахиль Кудрявцев', 'Лиана Марков', 'Изольда Черепов', 'Эльмира Хакамада', 'Клара Гольцев', 'Анна Жириновский', 'Ангелина Буданов', 'Вита Телицын', 'Агапия Сапожников', 'Фотиния Родин', 'Юна Цветаев', 'Авдотья Спиридонов', 'Ярослава Марков', 'Нина Филонов', 'Харитина Малевич', 'Софья Варламов', 'Александра Белов', 'Иона Цыплаков', 'Юдифь Устинов', 'Гелия Ливанов', 'Стефания Минаев', 'Устинья Вересаев', 'Анатолия Феоктистов', 'Жанна Райкин', 'Агния Елизаров', 'Павлина Червоненко', 'Харитина Абросимов', 'Диодора Чигиринский', 'Дина Хасбулатов', 'Агапия Цыганов', 'Елизавета Пименов']
['Grai Dạ Nguyệt', 'Bão Kim Liên', 'Bật Châu Mai', 'Banh Sa Lem', 'Khà Cát Hạ', 'Chương Đào Nguyên', 'Thẩm Cương', 'Cống Đan Tâm', 'Nguyễn Nguyệt Nga', 'Thiệu Lệ Thanh', 'Sỳ Nhật Dạ', 'Vĩnh Hải Hòa', 'Trịnh Lan Vy', 'Bán Hương Lan', 'Tông Hiền Nhi', 'Ra Bạch Loan', 'Bi Hằng Nga', 'Tiêu Đào Lan', 'Mèo Phương Tâm', 'Chung Ngọc Lệ', 'Ki Mỹ Nương', 'Ông Hạnh Dung', 'Cooi Trúc Vân', 'Cự Bảo Thy', 'Vũ Gia Nhi', 'Can Phú', 'Dư Diệu Huyền', 'Pà Thanh Nga', 'Nghi Thúy Ngà', 'Đa Bích Quỳnh', 'Mai Hạnh', 'Khiêm Diệu Chi']
['Débora Ocaña', 'Selene Palau', 'Úrsula Del Pozo', 'Guillermina Perelló', 'Vicenta Pedro', 'Esmeralda Chacón', 'Melisa Marquina', 'Prudencia Lorenzo', 'Odette Alberola', 'Paloma Gómez', 'Leire Carrera', 'Hebe Colom', 'Anaís Garay', 'Débora Bernabé', 'Olivia Cuevas', 'Melany Muro', 'Federica Góngora', 'Nora Tomé', 'Aurelia Guardia', 'Carina Coca', 'Odette Tejero', 'Aurelia Ballesteros', 'Dora Barrio', 'Belinda Infante', 'Graciela Mesa', 'Helena Contreras', 'Ermelinda Barco', 'Irene Palma', 'Yolanda Fábregas', 'Maribel Grau', 'Prudencia Saldaña', 'Brenda Paredes']
['ณัฐพร แก้วนำชัย', 'มัลลิกา คล่องแคล่ว', 'กานต์ชนก แก้วสว่าง', 'สมศรี กิตติไพศาล', 'ผ่องศรี งามสม', 'ปิยวรรณ จอมทอง', 'ศิริวิมล ไกรฤกษ์', 'กุลธิดา จรัสศรี', 'กนกอร เจริญดี', 'ชัญญานุช จิตรา', 'สลิลา เจริญศรี', 'งามพรรณ กัญจนรุจิ', 'ญาณิน จันทรวิโรจน์', 'อภิษฎา เกตุแก้ว', 'วรรณวิภา เข็มทอง', 'ชนัญชิดา จำรัส', 'จารุภา กัลยาณมิตร', 'รัญญา จิตต์ใจฉ่ำ', 'เสาวภา กฤษณะเศรณี', 'สุดารัตน์ เกษมสุข', 'พรพิมล แก้วใส', 'ศุภนิดา คุ้มวงษ์', 'ภาคินี จิรวัฒน์', 'อัจฉราพรรณ กังวานเจริญ', 'เนตรชนก จันทรานนท์', 'พรทิพย์ กรุณานนท์', 'ชฎาภรณ์ คำคง', 'พวงเพชร จิตต์ศรัทธา', 'สายสมร ครุฑทอง', 'กมลา กังวาน', 'สกุลรัตน์ กลิ่นหอม', 'วีณา แก้วตา']
['Carlota Odonnell', 'Ayla Mann', 'Dellia Kane', 'Elza Patrick', 'Isabelle King', 'Alaina Raymond', 'Kristian Gilliam', 'Fiona Rice', 'Diamond Velasquez', 'Channie Malone', 'Danae Slater', 'Kiya Vargas', 'Arlena Stanton', 'Hazelle Mcclain', 'Eleanore Nixon', 'Aretha Davidson', 'Ardath Sherman', 'Angelique Murphy', 'Kristyn Branch', 'Deena Lindsey', 'Elenora Schroeder', 'Inga Brady', 'Bebe Morrison', 'Belle Barber', 'Jesenia Glover', 'Gia Peterson', 'Angelita Lopez', 'Kristen Dillard', 'Christeen Burgess', 'Alexia Pena', 'Kay Langley', 'Emilee Allen']
['Fumiko Browning', 'Danielle Odom', 'Clementina Nielsen', 'Emmie Mcfarland', 'Jeanett Reid', 'Emaline Vega', 'Bessie Patrick', 'Charlene Montgomery', 'Daniella Miranda', 'Idabelle Decker', 'Kamilah Riddle', 'Ellamae Ewing', 'Gertie Cote', 'Hailee Burke', 'Elida Dotson', 'Caitlyn Dean', 'Keena Cantu', 'Cristen Clements', 'Genevra Flowers', 'Gretta Dickerson', 'Cherise Pugh', 'Karan Nichols', 'Aliyah Fischer', 'Claribel Dillard', 'Cher Briggs', 'Dovie Watson', 'Jenniffer Melendez', 'Justina Campbell', 'Krystal Thomas', 'Genoveva Ferrell', 'Dana Chen', 'Jeana Lynn']
```