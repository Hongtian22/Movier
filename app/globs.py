# the indices for each topic
topic_indices = [0, 1, 2, 4, 5, 7, 8, 9, 10, 15, 18, 19, 33, 34, 42, 45, 49,
                 52, 55, 56, 66, 67, 68, 71, 74, 83, 91, 94, 99,
                 106, 109, 113, 124, 130, 131, 133, 134, 137, 138, 144, 150,
                 151, 152, 154, 155, 158, 163, 164, 165, 172, 178, 179,
                 182, 183, 184, 186, 188, 189, 192, 193, 197, 198, 199]

# the names for each topic
topic_names = ["Relationship/Intimacy",
               "Negative Words I",
               "Conversational I",
               "Racist/Gang",
               "Army/Navy",
               "Sounds/Noise",
               "Royalty",
               "Science Fiction",
               "Family/Household",
               "Money/Bank",
               "Western",
               "Mob",
               "Sports",
               "Conversational II",
               "Holiday/Christmas",
               "Movie",
               "Spanish Language",
               "Music",
               "French Language I",
               "Religion",
               "Family/Religion I",
               "Politics/World",
               "War",
               "Myth/Religion",
               "Detective/Crime",
               "Negative Words II",
               "Modal Particles",
               "Horror/Fantasy",
               "Fight Club",
               "Myth",
               "Animals/Kids I",
               "Family/Religion II",
               "Ancient/Mid-evil",
               "Sailer/Pirate/Sea",
               "World/Documentary",
               "Negative Words III",
               "Sci-Fi/Fantasy",
               "Crime/Murder",
               "On the Road",
               "Hospital",
               "Aviation",
               "Police/Crime",
               "Babies/Family",
               "Conversational III",
               "Law/Justice",
               "Daily Life",
               "Animal/Kids",
               "Legend/FairyTale",
               "Western",
               "International",
               "Army/War",
               "Human Sound",
               "College/Fraternity",
               "Immigrant",
               "French Lang II",
               "World War II",
               "Musical/War",
               "Sailor/War",
               "Adventure",
               "Sex",
               "Crime",
               "Horror",
               "School"]


# the colors for each topic
topic_colors = ["#D250EC",
                "#78E63A",
                "#E6382C",
                "#5BADC1",
                "#404313",
                "#582154",
                "#E3A231",
                "#5D85E5",
                "#5FDA9C",
                "#DF3579",
                "#E899CC",
                "#B9A378",
                "#518A1B",
                "#4B1E1B",
                "#2F435F",
                "#824AA4",
                "#CEDC7F",
                "#902E1F",
                "#B1DBC3",
                "#E5D741",
                "#DB866A",
                "#63A27C",
                "#8A5C54",
                "#AB6828",
                "#797E8D",
                "#8A2E45",
                "#D94756",
                "#67E477",
                "#6B95CB",
                "#9D2F7A",
                "#A69D2E",
                "#98628F",
                "#2C352B",
                "#8768E1",
                "#877435",
                "#AC8DD7",
                "#6C705A",
                "#3A7E7B",
                "#6F441F",
                "#D96A8B",
                "#55E0C8",
                "#BACDDE",
                "#E47A28",
                "#DAB9AD",
                "#CF78D5",
                "#DF4CA8",
                "#495FA8",
                "#90C051",
                "#C3828B",
                "#BEE13F",
                "#388F46",
                "#DAD9A8",
                "#4ABA3A",
                "#D7B35F",
                "#443A74",
                "#48293E",
                "#315A31",
                "#69863D",
                "#D3B6D6",
                "#A1E093",
                "#D35731",
                "#73DDE7",
                "#D346C8"]

# name and color lookup dictionary for each topic
topics = {index: topic for index, topic in zip(topic_indices, topic_names)}
colors = {index: color for index, color in zip(topic_indices, topic_colors)}
