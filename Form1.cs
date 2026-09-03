using System;
using System.Drawing;
using System.Windows.Forms;

namespace MyWinFormsApp
{
    public partial class Form1 : Form
    {
        TextBox num1 = new TextBox();
        TextBox num2 = new TextBox();
        TextBox num3 = new TextBox();
        Button button = new Button();
        Label result = new Label();

        public Form1()
        {
            Text = "3 bogaturya";
            Width = 500;
            Height = 400;

            num1.Location = new Point(50, 30);
            num2.Location = new Point(50, 70);
            num3.Location = new Point(50, 110);

            button.Text = "Обчислити";
            button.Location = new Point(50, 150);

            result.Location = new Point(50, 200);
            result.AutoSize = true;

            button.Click += Calculate;

            Controls.Add(num1);
            Controls.Add(num2);
            Controls.Add(num3);
            Controls.Add(button);
            Controls.Add(result);
        }

        private void Calculate(object? sender, EventArgs e)
        {
            double a = double.Parse(num1.Text);
            double b = double.Parse(num2.Text);
            double c = double.Parse(num3.Text);

            double sum = a + b + c;
            double multiply = a * b * c;
            double subtract = a - b - c;

            result.Text =
                $"Додавання: {sum}\n" +
                $"Множення: {multiply}\n" +
                $"Віднімання: {subtract}";
        }
    }
}