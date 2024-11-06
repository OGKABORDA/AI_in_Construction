# TODO Найдите количество книг, которое можно разместить на дискете
stranic = 100
stroki = 50
simvoli = 25
value = 1.44 * 1024**2 # 1 мб - 1024 кб, 1 кб - 1024 байта
simvoli_v_knigge = simvoli * stroki * stranic * 4 # для хранения кода одного символна нужно 4 байта
kniggi_v_diskete = value // simvoli_v_knigge
print("Количество книг, помещающихся на дискету:",  int(kniggi_v_diskete))
