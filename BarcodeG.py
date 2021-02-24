import barcode
from barcode.writer import ImageWriter
barcode_writer = ImageWriter()
Product_number="productnumberX123"
ean = barcode.codex.Code39(Product_number, barcode_writer,  add_checksum=False)
filename = ean.save(f'{Product_number}')
