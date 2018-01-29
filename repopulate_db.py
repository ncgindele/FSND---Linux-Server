from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Item, Category

engine = create_engine('sqlite:///catalog.db')
#engine = create_engine('postgresql://catalog:papaya@localhost/catalog')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

firstUser = User(name="Jester Thomas", email="barb@aol.com", picture="https://upload.wikimedia.org/wikipedia/commons/1/1e/David-Bowie_Early.jpg")
session.add(firstUser)
session.commit()

firstCat = Category(name="David Bowie", user_id=firstUser.id)
session.add(firstCat)
session.commit()

item1 = Item(name='Ziggy Stardust and the Spiders From Mars', year=1972, icon='https://upload.wikimedia.org/wikipedia/en/0/01/ZiggyStardust.jpg', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget quam non nulla sodales laoreet. Etiam nec ipsum ac velit laoreet sodales. Sed efficitur hendrerit risus ut suscipit. Morbi vel nulla in urna cursus varius. Curabitur facilisis, tellus ut scelerisque mollis, est augue lacinia lorem, at imperdiet urna tortor ac felis. Etiam efficitur quam eget felis lacinia, eu pretium ligula maximus. Donec est ex, molestie quis ultrices sed, hendrerit id nibh.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item1)
session.commit()

item5 = Item(name='Station to Station', year=1976, icon='https://upload.wikimedia.org/wikipedia/en/9/97/Station_to_Station_cover.jpg', description="Cras in erat nulla. Donec vestibulum gravida leo, eget ultrices sapien maximus non. Duis varius vitae massa vitae varius. Phasellus ornare risus ac maximus ullamcorper. Nulla congue lacus vitae est faucibus iaculis ac a ex. Mauris id suscipit lacus. Aliquam neque tortor, cursus ut vehicula a, porttitor cursus nibh. Sed et nunc quam. Ut dignissim, mi ac ultricies mattis, arcu purus blandit enim, non iaculis erat sapien sed tellus. Nulla facilisi. Pellentesque non tempus lectus. Duis molestie sapien in leo fermentum, lobortis eleifend felis pharetra. Donec vel mollis ex, ac congue sem.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item5)
session.commit()

item6 = Item(name='Heroes', year=1977, icon='https://upload.wikimedia.org/wikipedia/en/7/7b/David_Bowie_-_Heroes.png', description="In nec dictum odio, sit amet rutrum justo. Cras eget gravida dolor, vitae facilisis elit. Nullam nec consectetur quam, et rutrum nibh. Proin sed dapibus elit. Integer ultrices, augue in faucibus consectetur, neque felis iaculis sapien, vel scelerisque dui neque eget arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras quam eros, rhoncus finibus lacus ac, sollicitudin egestas lectus. Cras vitae tristique massa. Curabitur at nibh ultricies, fermentum eros vitae, venenatis arcu. Nunc sodales interdum dui sit amet rhoncus. Integer tempor et eros ac tempor.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item6)
session.commit()

item7 = Item(name="Low", year=1977, icon='https://upload.wikimedia.org/wikipedia/en/9/93/Low_%28album%29.jpg', description="Aliquam erat volutpat. In blandit dolor at aliquam pulvinar. Donec interdum diam nulla, eget iaculis eros efficitur id. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam ornare, justo eget hendrerit interdum, libero turpis elementum odio, vitae tincidunt purus lorem nec libero. Phasellus in erat vestibulum, ullamcorper purus eu, elementum urna. Vestibulum vel lectus molestie erat congue lobortis sed a nulla. Ut luctus et sem vitae dictum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi fermentum libero ut lacinia fringilla. Praesent tellus arcu, sodales vitae erat quis, placerat tincidunt tellus.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item7)
session.commit()

secondCat = Category(name = "The Velvet Underground", user_id=firstUser.id)
session.add(secondCat)
session.commit()

item2 = Item(name='The Velvet Underground & Nico', year=1967, icon='https://upload.wikimedia.org/wikipedia/en/0/0c/Velvet_Underground_and_Nico.jpg', description="In convallis ex ut nunc fringilla dapibus. Fusce vel tortor dapibus lorem auctor semper. Nulla eu risus eu neque facilisis sodales. Aliquam auctor elit eget diam aliquet rutrum. Morbi efficitur, leo et sagittis aliquam, risus mi ultrices dui, ut sagittis orci massa a lectus. In efficitur sodales justo eget aliquam. Donec a laoreet metus, eget porta sapien. Vestibulum in laoreet purus, at iaculis ligula. Sed in ipsum imperdiet, bibendum erat nec, convallis lacus. Quisque pellentesque at magna eget blandit. Aenean aliquet posuere maximus. Nam sollicitudin enim et dui fermentum, ut porta lacus volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent velit tellus, rutrum id sollicitudin eu, ultrices eget eros.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item2)
session.commit()

item3 = Item(name='White Light/White Heat', year=1968, icon='https://upload.wikimedia.org/wikipedia/en/b/b6/VUToySoldiers.jpg', description="Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas tempor feugiat turpis ac pulvinar. Fusce et nibh nunc. Integer aliquam eleifend felis eu elementum. Proin eu tellus faucibus sem interdum dignissim vel sed tellus. Morbi vulputate egestas ipsum, et fringilla nunc hendrerit sed. Cras facilisis ipsum pulvinar sollicitudin dapibus. Mauris euismod consectetur eros, a vehicula lacus rhoncus eget. Praesent sed ullamcorper nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ut lorem interdum, fermentum ligula ut, dapibus purus. Integer in ligula ultrices, placerat sem nec, ornare dui.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item3)
session.commit()

item4 = Item(name='The Velvet Underground', year=1969, icon='https://upload.wikimedia.org/wikipedia/en/9/9a/Velvetundergroundthirdalbum.jpg', description="Nunc vel tristique nisi. Nullam feugiat lorem nec metus blandit venenatis vitae quis ante. Aliquam fermentum diam lectus, in consequat turpis sodales porttitor. Aliquam posuere neque faucibus sollicitudin maximus. Etiam elementum sagittis dapibus. Quisque pretium suscipit justo. Donec congue diam nibh, pulvinar mollis lectus mattis ac.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item4)
session.commit()

firstCat = Category(name="Charles Mingus", user_id=firstUser.id)
session.add(firstCat)
session.commit()

item1 = Item(name='Pithecanthropus Erectus', year=1956, icon='https://upload.wikimedia.org/wikipedia/en/9/96/Pithecanthropus_Erectus.jpg', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget quam non nulla sodales laoreet. Etiam nec ipsum ac velit laoreet sodales. Sed efficitur hendrerit risus ut suscipit. Morbi vel nulla in urna cursus varius. Curabitur facilisis, tellus ut scelerisque mollis, est augue lacinia lorem, at imperdiet urna tortor ac felis. Etiam efficitur quam eget felis lacinia, eu pretium ligula maximus. Donec est ex, molestie quis ultrices sed, hendrerit id nibh.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item1)
session.commit()

item5 = Item(name='The Clown', year=1957, icon='https://upload.wikimedia.org/wikipedia/en/b/bb/Charles_Mingus-The_Clown_Album_Cover.jpg', description="Cras in erat nulla. Donec vestibulum gravida leo, eget ultrices sapien maximus non. Duis varius vitae massa vitae varius. Phasellus ornare risus ac maximus ullamcorper. Nulla congue lacus vitae est faucibus iaculis ac a ex. Mauris id suscipit lacus. Aliquam neque tortor, cursus ut vehicula a, porttitor cursus nibh. Sed et nunc quam. Ut dignissim, mi ac ultricies mattis, arcu purus blandit enim, non iaculis erat sapien sed tellus. Nulla facilisi. Pellentesque non tempus lectus. Duis molestie sapien in leo fermentum, lobortis eleifend felis pharetra. Donec vel mollis ex, ac congue sem.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item5)
session.commit()

item6 = Item(name='Mingus Ah Uhm', year=1959, icon='https://upload.wikimedia.org/wikipedia/en/6/65/Mingus_Ah_Um_-_Charles_Mingus.jpg', description="In nec dictum odio, sit amet rutrum justo. Cras eget gravida dolor, vitae facilisis elit. Nullam nec consectetur quam, et rutrum nibh. Proin sed dapibus elit. Integer ultrices, augue in faucibus consectetur, neque felis iaculis sapien, vel scelerisque dui neque eget arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras quam eros, rhoncus finibus lacus ac, sollicitudin egestas lectus. Cras vitae tristique massa. Curabitur at nibh ultricies, fermentum eros vitae, venenatis arcu. Nunc sodales interdum dui sit amet rhoncus. Integer tempor et eros ac tempor.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item6)
session.commit()

item7 = Item(name="Black Saint and the Sinner Lady", year=1963, icon='https://upload.wikimedia.org/wikipedia/en/2/2e/Mingus_Black_Saint.jpg', description="Aliquam erat volutpat. In blandit dolor at aliquam pulvinar. Donec interdum diam nulla, eget iaculis eros efficitur id. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam ornare, justo eget hendrerit interdum, libero turpis elementum odio, vitae tincidunt purus lorem nec libero. Phasellus in erat vestibulum, ullamcorper purus eu, elementum urna. Vestibulum vel lectus molestie erat congue lobortis sed a nulla. Ut luctus et sem vitae dictum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi fermentum libero ut lacinia fringilla. Praesent tellus arcu, sodales vitae erat quis, placerat tincidunt tellus.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item7)
session.commit()

secondCat = Category(name = "Beck", user_id=firstUser.id)
session.add(secondCat)
session.commit()

item2 = Item(name='Mellow Gold', year=1994, icon='https://upload.wikimedia.org/wikipedia/en/3/3e/MellowGold.jpg', description="In convallis ex ut nunc fringilla dapibus. Fusce vel tortor dapibus lorem auctor semper. Nulla eu risus eu neque facilisis sodales. Aliquam auctor elit eget diam aliquet rutrum. Morbi efficitur, leo et sagittis aliquam, risus mi ultrices dui, ut sagittis orci massa a lectus. In efficitur sodales justo eget aliquam. Donec a laoreet metus, eget porta sapien. Vestibulum in laoreet purus, at iaculis ligula. Sed in ipsum imperdiet, bibendum erat nec, convallis lacus. Quisque pellentesque at magna eget blandit. Aenean aliquet posuere maximus. Nam sollicitudin enim et dui fermentum, ut porta lacus volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent velit tellus, rutrum id sollicitudin eu, ultrices eget eros.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item2)
session.commit()

item3 = Item(name='Odelay', year=1996, icon='https://upload.wikimedia.org/wikipedia/en/f/f4/Odelay.jpg', description="Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas tempor feugiat turpis ac pulvinar. Fusce et nibh nunc. Integer aliquam eleifend felis eu elementum. Proin eu tellus faucibus sem interdum dignissim vel sed tellus. Morbi vulputate egestas ipsum, et fringilla nunc hendrerit sed. Cras facilisis ipsum pulvinar sollicitudin dapibus. Mauris euismod consectetur eros, a vehicula lacus rhoncus eget. Praesent sed ullamcorper nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ut lorem interdum, fermentum ligula ut, dapibus purus. Integer in ligula ultrices, placerat sem nec, ornare dui.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item3)
session.commit()

item4 = Item(name='Mutations', year=1998, icon='https://upload.wikimedia.org/wikipedia/en/3/31/Mutations.jpg', description="Nunc vel tristique nisi. Nullam feugiat lorem nec metus blandit venenatis vitae quis ante. Aliquam fermentum diam lectus, in consequat turpis sodales porttitor. Aliquam posuere neque faucibus sollicitudin maximus. Etiam elementum sagittis dapibus. Quisque pretium suscipit justo. Donec congue diam nibh, pulvinar mollis lectus mattis ac.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item4)

session.commit()

firstCat = Category(name="Talking Heads", user_id=firstUser.id)
session.add(firstCat)
session.commit()

item1 = Item(name='Talking Heads: 77', year=1977, icon='https://upload.wikimedia.org/wikipedia/commons/b/be/Talking_Heads_77.jpg', description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eget quam non nulla sodales laoreet. Etiam nec ipsum ac velit laoreet sodales. Sed efficitur hendrerit risus ut suscipit. Morbi vel nulla in urna cursus varius. Curabitur facilisis, tellus ut scelerisque mollis, est augue lacinia lorem, at imperdiet urna tortor ac felis. Etiam efficitur quam eget felis lacinia, eu pretium ligula maximus. Donec est ex, molestie quis ultrices sed, hendrerit id nibh.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item1)
session.commit()

item5 = Item(name='More Songs About Buildings and Food', year=1978, icon='https://upload.wikimedia.org/wikipedia/en/7/75/TalkingHeadsMoreSongsAboutBuildingsandFood.jpg', description="Cras in erat nulla. Donec vestibulum gravida leo, eget ultrices sapien maximus non. Duis varius vitae massa vitae varius. Phasellus ornare risus ac maximus ullamcorper. Nulla congue lacus vitae est faucibus iaculis ac a ex. Mauris id suscipit lacus. Aliquam neque tortor, cursus ut vehicula a, porttitor cursus nibh. Sed et nunc quam. Ut dignissim, mi ac ultricies mattis, arcu purus blandit enim, non iaculis erat sapien sed tellus. Nulla facilisi. Pellentesque non tempus lectus. Duis molestie sapien in leo fermentum, lobortis eleifend felis pharetra. Donec vel mollis ex, ac congue sem.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item5)
session.commit()

item6 = Item(name='Fear of Music', year=1979, icon='https://upload.wikimedia.org/wikipedia/en/8/88/Talking_Heads-Fear_of_Music.jpg', description="In nec dictum odio, sit amet rutrum justo. Cras eget gravida dolor, vitae facilisis elit. Nullam nec consectetur quam, et rutrum nibh. Proin sed dapibus elit. Integer ultrices, augue in faucibus consectetur, neque felis iaculis sapien, vel scelerisque dui neque eget arcu. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras quam eros, rhoncus finibus lacus ac, sollicitudin egestas lectus. Cras vitae tristique massa. Curabitur at nibh ultricies, fermentum eros vitae, venenatis arcu. Nunc sodales interdum dui sit amet rhoncus. Integer tempor et eros ac tempor.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item6)
session.commit()

item7 = Item(name="Remain in Light", year=1980, icon='https://upload.wikimedia.org/wikipedia/en/2/2d/TalkingHeadsRemaininLight.jpg', description="Aliquam erat volutpat. In blandit dolor at aliquam pulvinar. Donec interdum diam nulla, eget iaculis eros efficitur id. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nam ornare, justo eget hendrerit interdum, libero turpis elementum odio, vitae tincidunt purus lorem nec libero. Phasellus in erat vestibulum, ullamcorper purus eu, elementum urna. Vestibulum vel lectus molestie erat congue lobortis sed a nulla. Ut luctus et sem vitae dictum. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Morbi fermentum libero ut lacinia fringilla. Praesent tellus arcu, sodales vitae erat quis, placerat tincidunt tellus.", category_id=firstCat.id, user_id=firstUser.id)
session.add(item7)
session.commit()

secondCat = Category(name = "Iggy Pop", user_id=firstUser.id)
session.add(secondCat)
session.commit()

item2 = Item(name='The Idiot', year=1977, icon='https://upload.wikimedia.org/wikipedia/en/9/9d/Iggy_Pop_-_The_Idiot.png', description="In convallis ex ut nunc fringilla dapibus. Fusce vel tortor dapibus lorem auctor semper. Nulla eu risus eu neque facilisis sodales. Aliquam auctor elit eget diam aliquet rutrum. Morbi efficitur, leo et sagittis aliquam, risus mi ultrices dui, ut sagittis orci massa a lectus. In efficitur sodales justo eget aliquam. Donec a laoreet metus, eget porta sapien. Vestibulum in laoreet purus, at iaculis ligula. Sed in ipsum imperdiet, bibendum erat nec, convallis lacus. Quisque pellentesque at magna eget blandit. Aenean aliquet posuere maximus. Nam sollicitudin enim et dui fermentum, ut porta lacus volutpat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent velit tellus, rutrum id sollicitudin eu, ultrices eget eros.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item2)
session.commit()

item3 = Item(name='Post Pop Depression', year=2016, icon='https://upload.wikimedia.org/wikipedia/en/e/e1/Post_Pop_Depression_%28Front_Cover%29.png', description="Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Maecenas tempor feugiat turpis ac pulvinar. Fusce et nibh nunc. Integer aliquam eleifend felis eu elementum. Proin eu tellus faucibus sem interdum dignissim vel sed tellus. Morbi vulputate egestas ipsum, et fringilla nunc hendrerit sed. Cras facilisis ipsum pulvinar sollicitudin dapibus. Mauris euismod consectetur eros, a vehicula lacus rhoncus eget. Praesent sed ullamcorper nisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; In ut lorem interdum, fermentum ligula ut, dapibus purus. Integer in ligula ultrices, placerat sem nec, ornare dui.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item3)
session.commit()

item4 = Item(name='Lust for Life', year=1977, icon='https://upload.wikimedia.org/wikipedia/en/7/72/IggyPopLustForLife.jpg', description="Nunc vel tristique nisi. Nullam feugiat lorem nec metus blandit venenatis vitae quis ante. Aliquam fermentum diam lectus, in consequat turpis sodales porttitor. Aliquam posuere neque faucibus sollicitudin maximus. Etiam elementum sagittis dapibus. Quisque pretium suscipit justo. Donec congue diam nibh, pulvinar mollis lectus mattis ac.", category_id=secondCat.id, user_id=firstUser.id)
session.add(item4)

session.commit()
