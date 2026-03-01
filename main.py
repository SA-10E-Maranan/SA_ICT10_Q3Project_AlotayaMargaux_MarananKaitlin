# Skills Test 3rd Quarter
from pyscript import document

# Players from each team
lists = {
	"Heartslabyul": ["Rosehearts, Riddle (Leader)", "Chua, Reese Blesilda W.", "Clover, Trey", "Diamond, Cater", "Macala, Sophia Issabel C.", "Maranan, Kaitlin Pia G.", "Spade, Deuce", "Trappola, Ace"],
	"Octavinelle": ["Ashengrotto, Azul (Leader)", "Estabillo, Carl Jaden M.", "Leech, Floyd", "Leech, Jade", "Lusica, Alyza Kate O.", "Musor, Hanna Yasmin M.", "Mito, Yuuta", "Razonable, Matt Sky L."],
	"Ignihyde": ["Shroud, Idia (Leader)", "Alwit, David Andrew K.", "Chavez, Cen Mar Gabriel D.", "Gale, Benjamin Miguel B.", "Ramirez, Aion P.", "Shroud, Ortho", "Tiwari, Kushdeep S."],
	"Savanaclaw": ["Kingscholar, Leona (Leader)", "Brar, Opdesh S.", "Bucchi, Ruggie", "De Los Santos, Samuel Joshua", "Howl, Jack", "Omnes, Wilwen Benedict P.", "Platon, Travis Reiley"],
	"Diasomnia": ["Draconia, Malleus (Leader)", "Alotaya, Margaux J.", "Fernandez, Lesvie Mae A.", "Oreiro, Rochel M.", "Vanrouge, Lilia", "Vanrouage, Silver", "Zigvolt, Sebek"],
    "Pomefiore": ["Schoenheit, Vil (Leader)", "Felmier, Epel", "Garcia, Joshua Melroy", "Hunt, Rook", "Montemayor, Padme Havilah A.", "Silleza, Lucilind A.", "Villanueva, Sofia Leona S."],
    "Scarabia": ["Al-Asim, Kalim (Leader)", "Faner, Janinna Arelie F.", "Kaur, Simrat", "Laeda, Lewis B.", "Macas, Zaia Chryzelle D.", "Salvador, Eris Russell I.", "Viper, Jamil", "Oujou, Yuuna"],
    "Ramshackle": ["Enma, Yuuken (Leader)", "Aquino, Shean Terrenze O.", "Gill, Ekamnoor K.", "Grim", "Hirasaka, Yuuka", "Kuroki, Yuuya", "Salvador, Toni Rianne M."],
}

output = document.getElementById("output")
for title, names in lists.items():
    output.innerHTML += f"<h5 class='text-center mb-1'>{title}</h5>"
    for i, name in enumerate(names, 1):
        output.innerHTML += f"{i}. {name}<br>"
    output.innerHTML += "<br>"
