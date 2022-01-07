from fpdf import FPDF
import os

dir = os.path.dirname(os.path.abspath(__file__))
dir_font =os.path.join(dir,r'dejavufont\\ttf\\DejaVuSansCondensed.ttf')

class PDF(FPDF):
    def header(self):
        # logo
        # self.image('../static/images/rau2.jpg',8,4,25)
        # font
        self.add_font('DejaVu','B', dir_font , uni=True)
        self.set_font('DejaVu','B',15)
        # padding
        # title
        self.cell(0,0,'',align='C')
        # ngắt dòng
        self.ln(1)
    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        # số trang
        self.cell(0,10,f'Trang {self.page_no()}',align='C')


pdf = PDF('P', 'mm' , (100,200))

# tạo tự động ngắt trang
pdf.set_auto_page_break(auto=True, margin=15)

# thêm trang
pdf.add_page()
# title

pdf.set_font('DejaVu', 'B', 16)
pdf.cell(30)
pdf.cell(10, 10, 'Hóa đơn',ln=True)

# thêm font chữ
pdf.set_font('DejaVu', 'B', 14.0)
# nội dung
# width 
# height

data = [['Mã đơn hàng:121212', 'Thời gian:121212', 'Địa chỉ:121212', 'Tên:12121','Số điện thoại:12121212']]

for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(140, 10, str(datum),ln=True)


pdf.cell(0, 20, '-------------------------------------------------', ln=True)
epw = pdf.w - 2 * pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
col_width = epw / 4

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.

data = [['Sản phẩm', 'SL', 'Đơn giá', 'Tổng tiền'],
        ['Ca rot', '12', 34, '123'],
        ['Khoai tay', '12', 45, '12321'],
        ['Ca tim', '12', 19, '12323'],
        ['Ca tim', '12', 19, '12323'],
['Ca tim', '12', 19, '12323'],['Ca tim', '12', 19, '12323'],['Ca tim', '12', 19, '12323'],['Ca tim', '12', 19, '12323'],['Ca tim', '12', 19, '12323'],
        ]


# Text height is the same as current font size
th = pdf.font_size
pdf.ln(0)

pdf.set_font('DejaVu', 'B', 10.0)
pdf.ln(0.5)

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2 * th, str(datum), align='R')

    pdf.ln(2 * th)

pdf.set_font('DejaVu','B',14.0)
pdf.cell(10, 20, '-------------------------------------------------', ln=True)
pdf.cell(57, 10,'Tổng')
pdf.cell(0, 10,'12121212',ln=True)

pdf.set_font('DejaVu','B',14.0)
pdf.cell(10, 20, '-------------------------------------------------', ln=True)
pdf.cell(57, 10,'Ship')
pdf.cell(0, 10,'12121212',ln=True)

pdf.set_font('DejaVu','B',14.0)
pdf.cell(10, 20, '--------------------------------------------------', ln=True)
pdf.cell(57, 10,'Tổng thanh toán')
pdf.cell(0, 10,'12121212',ln=True)

pdf.output('pdf_test.pdf')



