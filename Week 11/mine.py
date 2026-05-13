# A module of my own nonsense



def input_validate[T](target_type: type[T] = str,message = ">>> ")->T:
    var = None
    while True:
        try:
            var = target_type(input(message))
        except:
            continue
        else:
            break
    return var
