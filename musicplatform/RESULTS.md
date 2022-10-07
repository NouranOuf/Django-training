* create some artists
    from artists.models import Artist
    from albums.models import Album 
    obj = Artist (stage_name='amr diab' , social_link='https://www.instagram.com/amrdiab/')
    obj.save()
    obj1 = Artist (stage_name='mohamed mounir' , social_link='https://www.instagram.com/mounirofficial/')
    obj1.save()
	obj2 = Artist (stage_name='shereen' , social_link='https://www.instagram.com/sherine/')
    obj2.save()
    obj3 = Artist (stage_name='wael gassar' , social_link='https://www.instagram.com/waeljassarofficial/')
    obj3.save()
    obj4 = Artist (stage_name='assala' , social_link='https://www.instagram.com/mounirofficial/')
    obj4.save()
    obj5 = Artist (stage_name='tamer hosny' , social_link='https://www.instagram.com/assala_official/')
    obj5.save()
    obj6 = Artist (stage_name='bahaa sultan' , social_link='https://www.instagram.com/bahaasultanofficial/')
    obj6.save()
* list down all artists
    Artist.objects.all()
        -Output:
          <QuerySet [<Artist: amr diab>, <Artist: mohamed mounir>, <Artist: shereen>, <Artist: wael gassar>, <Artist: assala>, <Artist; bahaa sultan>]>
	
* list down all artists sorted by name
    Artist.objects.all().order_by('stage_name')
        -Output:
          <QuerySet [<Artist: amr diab>, <Artist: assala>, <Artist: bahaa sultan>, <Artist: mohamed nounir>, <Artist: shereen> , <Artist: wael gassar>]> 
	
* list down all artists whose name starts with `a`
    Artist.objects.filter(stage_name__istartswith='a')
        -Output:
          <QuerySet [<Artist: amr diab>, <Artist: assala>]>

* in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)

    first approach :
        obj7 = Artist.objects.get(id=1)
        obj7.album_set.create(name='el lela',release_date='2010-12-11',cost=1200)
        obj7.album_set.all()

    second approach :
        album = Album.objects.create(artist_id=obj7 , cost=1000)
        obj8 = Artist.objects.get(id=2)
        Album.objects.create(artist_id=obj8,name='hallo',cost=1000)
        Album.objects.create(artist_id=obj8,creation_date='2022-10-07',release_date='2022-10-10',cost=1000)
        obj9 = Artist.objects.get(id=3)
        Album.objects.create(artist_id=obj9 ,cost=1000)
        obj10 = Artist.objects.get(id=4)
        Album.objects.create(artist_id=obj10 , cost=1000)
        Album.objects.create(artist_id=obj10 ,name='shbabek',cost=1000)
        Album.objects.create(artist_id=obj10 ,name='manazel',cost=1000)
        obj11 = Artist.objects.get(id=3)
        Album.objects.create(artist_id=obj9,creation_date='2022-10-07' ,cost=1000)
        Album.objects.create(artist_id=obj7,name='test',release_date='2022-10-07',cost=20)

* get the latest released album
    Album.objects.values('name' ,'release_date' ).latest('release_date')
    -or to elemenate the nulls
    Album.objects.filter(release_date__isnull=False).values('name' ,'release_date' ).latest('release_date')
    -Output:
        {"name": "New Album', 'release_date': datetime.date(2022, 10, 10)}
           
* get all albums released before today
    from datetime import date, datetime
    Album.objects.filter(release_date__lt = date.today()).values('name' , 'release_date')
        -Output:
          [
          {'name': 'el lela', 'release_date': datetime.date(2010, 12, 11)}, 
          {'name': 'New Album', 'release_date': datetime.date(2022, 10, 6)}, 
          {"name" : "hallo', "release_date": datetime.date(2022, 10, 6)}, 
          {'name': 'New Album', 'release_date': datetime.date(2022, 10, 6)},
          {"name": "shbabek", "release _date': datetime.date(2022, 10, 6)}, 
          {'name': 'manazel', 'release_date': datetime.date(2022, 10, 6)}}]
          
* get all albums released today or before but not after today
    Album.objects.filter(release_date__lte = date.today()).values('name' , 'release_date')
        -Output:
          [
          {'name': 'el lela', 'release_date': datetime.date(2010, 12, 11)}, 
          {'name': 'New Album', 'release_date': datetime.date(2022, 10, 6)}, 
          {"name" : "hallo', "release_date": datetime.date(2022, 10, 6)}, 
          {'name': 'New Album', 'release_date': datetime.date(2022, 10, 6)},
          {"name": "shbabek", "release _date': datetime.date(2022, 10, 6)}, 
          {'name': 'manazel', 'release_date': datetime.date(2022, 10, 6)},
           'name': 'test', 'release_date': datetime.date(2022, 10, 7)}>

* count the total number of albums
    Album.objects.count()
        -output:9

* in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)
    from django.db.models import Subquery
    Album.objects.all().filter(artist_id__in = Subquery(Artist.objects.values('pk')))
    Album.objects.all().select_related('artist_id')
        -output:
        [
        {'name': 'el lela', 'release_date': datetime.date(2010, 12, 11)}, 
        {'name': 'New Album', 'release_date': datetime.date(2022, 10, 6)}, 
        {"name" : "hallo', "release_date": datetime.date(2022, 10, 6)}, 
        {'name': 'New Album', 'release_date': datetime.date(2022, 10, 6)},
        {"name": "shbabek", "release _date': datetime.date(2022, 10, 6)}, 
        {'name': 'manazel', 'release_date': datetime.date(2022, 10, 6)}}>

    -with artist name :
    obj13 = Artist.objects.all().filter(pk__in = Subquery(Album.objects.values('artist_id')))
    obj14 = Album.objects.all().select_related('artist_id')
    for artist in obj13:
        print('Artist:',artist)
        for album in obj14:
            if(artist==album.artist_id):
                print(album)
    -output:
    Artist:amr diab
    el lela 
    New Album
    test
    Artist:mohamed mounir
    hallo
    New album
    Artist:shereen
    New album
    Artist:wael gassar
    New album
    shbabek
    manazel
          
* list down all albums ordered by cost then by name (cost has the higher priority)
    Album.objects.order_by('cost', 'name')
    -Output:
      <QuerySet [<Album: test>, <Album: New Album, <Album: New Album>, <Album: New Album>, <Album: hallo>, 
      <Album: manazel>, <Album: shbabelo, <Album: el lela>, <Album: New Album]>
 
