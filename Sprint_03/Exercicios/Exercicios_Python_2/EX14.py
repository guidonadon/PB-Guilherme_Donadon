def fun(*args, **kwargs):
    for termo in args:
        print(termo)
        
    for item in kwargs.values():
        print(item)

fun(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
