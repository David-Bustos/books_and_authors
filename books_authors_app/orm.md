 # Consulta: crea 5 libros con los siguientes nombres: C Sharp, Java, Python, PHP, Ruby

Author.objects.create(first_name = 'Jane', last_name = 'Austen')
Author.objects.create(first_name = 'Emily', last_name = 'Dickinson')
Author.objects.create(first_name = 'Fyodor', last_name = 'Dostoevksy')
Author.objects.create(first_name = 'William', last_name = 'Shakespeare')
Author.objects.create(first_name = 'Lau', last_name = 'Tzu')

 # Consulta: Crea 5 autores diferentes: Jane Austen, Emily Dickinson, Fyodor Dostoevksy, William Shakespeare, Lau Tzu

Book.objects.create(title = 'C Sharp')
Book.objects.create(title = 'Java')
Book.objects.create(title = 'Python')
Book.objects.create(title = 'PHP')
Book.objects.create(title = 'Ruby')

 # Agregue un nuevo campo de texto en la tabla de autores llamado 'notas'.

notes = models.TextField(blank=True)

 # Cree y ejecute los archivos de migración para actualizar la tabla en su base de datos.

python manage.py makemigration
python manage.py migrate

 # Consulta: cambie el nombre del libro de C Sharp a C #

b = Book.objects.get(id=1)
b.title = "C #"
b.save()

 # Consulta: cambie el nombre del cuarto autor a Bill

a = Author.objects.get(id=4)
a.first_name = "Bill"
a.save()

 # Consulta: Asigna el primer autor a los primeros 2 libros.

b1 = Book.objects.get(id=1)
b2 = Book.objects.get(id=2)
a1 = Author.objects.get(id=1)
b1.authors.add(a1)
b2.authors.add(a1)

 # Consulta: Asigne el segundo autor a los primeros 3 libros.

b1 = Book.objects.get(id=1)
b2 = Book.objects.get(id=2)
b3 = Book.objects.get(id=3)
a2 = Author.objects.get(id=2)
b1.authors.add(a2)
b2.authors.add(a2)
b3.authors.add(a2)

 # Consulta: Asigna el tercer autor a los primeros 4 libros.

b1 = Book.objects.get(id=1)
b2 = Book.objects.get(id=2)
b3 = Book.objects.get(id=3)
b4 = Book.objects.get(id=4)
a3 = Author.objects.get(id=3)
b1.authors.add(a3)
b2.authors.add(a3)
b3.authors.add(a3)
b4.authors.add(a3)

 # Consulta: Asigne el cuarto autor a los primeros 5 libros (o en otras palabras, todos los libros)

b1 = Book.objects.get(id=1)
b2 = Book.objects.get(id=2)
b3 = Book.objects.get(id=3)
b4 = Book.objects.get(id=4)
b5 = Book.objects.get(id=5)
a4 = Author.objects.get(id=4)
b1.authors.add(a4)
b2.authors.add(a4)
b3.authors.add(a4)
b4.authors.add(a4)
b5.authors.add(a4)

 # Consulta: recupera a todos los autores del tercer libro

b3.authors.all()

 # Consulta: eliminar al primer autor del tercer libro

b3.authors.remove(a1)

 # Consulta: Agregue el quinto autor como uno de los autores del segundo libro.

a5 = Author.objects.get(id=5)
b2.authors.add(a5)

 # Consulta: Encuentra todos los libros de los que el tercer autor es parte

a3.books.all()

 # Consulta: Encuentra todos los autores que contribuyeron al quinto libro.

b5.authors.all()