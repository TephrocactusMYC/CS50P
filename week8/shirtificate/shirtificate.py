from fpdf import FPDF


class Shirt:
    """创建一个“I took CS50”T恤证书实例"""

    def __init__(self, name):
        self.name = name
        self.tailor()

    def tailor(self):
        """使用当前实例的详情创建一个PDF"""
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # 设置字体和在页面顶部添加标题
        pdf.set_font("helvetica", "B", size=46)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()

        # 添加并居中T恤图片
        pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"A Harvard shirt with the words: {self.name} took CS50",
        )

        # 设置字体并在T恤上方添加文本
        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")

        # 将PDF保存到文件
        pdf.output("shirtificate.pdf")

    @classmethod
    def get(cls):
        """工厂方法：用于实例化T恤证书对象"""
        name = input("Full name: ").strip()
        return cls(name)


def main():
    # 调用工厂方法生成对象
    shirt = Shirt.get()


if __name__ == "__main__":
    main()
