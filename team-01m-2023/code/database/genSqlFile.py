from faker import Faker
from faker.providers import person
import random

fake = Faker()
fake.add_provider(person)

pronounList = ['he/him', 'they/them', 'she/her', 'he/they', 'she/they', 'any pronouns']
descriptionList = ['Looking to climb and have fun', 'Here for a good time', 'Training for a competition']
locationList = ['Brooklyn Boulders', 'Block 37', 'Avondale', 'Uptown', 'Humboldt', 'Movement']
climbTypeList = ['Bouldering', 'Top Rope', 'Lead Climbing']
experienceLevelList = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
daysAvailableList = ['Su', 'M', 'Tu', 'W', 'Th', 'F', 'Sa']
outFile = open('users_post.sql', 'w')

outFile.write("CREATE TABLE IF NOT EXISTS `users_post` (`id` BIGINT AUTO_INCREMENT PRIMARY KEY, `name` varchar(30) NOT NULL, `pron` varchar(15) NOT NULL, `desc` longtext, `gymLocations` longtext, `climbType` longtext, `expLevel` longtext, `availability` longtext, `username` longtext);\n\n")

for _ in range(50):
    name = fake.name()
    pron = random.choice(pronounList)
    desc = random.choice(descriptionList)
    gymLocations = ', '.join(fake.random_elements(elements=locationList, unique=True))
    climbType = ', '.join(fake.random_elements(elements=climbTypeList, unique=True))
    expLevel = random.choice(experienceLevelList)
    availability = ', '.join(fake.random_elements(elements=daysAvailableList, unique=True))
    username = fake.first_name() + '#' + fake.numerify(text='####')
    outFile.write(f"INSERT INTO users_post (`name`, `pron`, `desc`, `gymLocations`, `climbType`, `expLevel`, `availability`, `username`) VALUES ('{name}', '{pron}', '{desc}', '{gymLocations}', '{climbType}', '{expLevel}', '{availability}', '{username}');\n")

outFile.close()