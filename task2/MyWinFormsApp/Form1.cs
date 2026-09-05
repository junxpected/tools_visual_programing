using System;
using System.Windows.Forms;

namespace MyWinFormsApp
{
    public partial class Form1 : Form
    {
        TextBox waterOld = new TextBox();
        TextBox waterNew = new TextBox();
        TextBox waterTariff = new TextBox();

        TextBox electricityOld = new TextBox();
        TextBox electricityNew = new TextBox();
        TextBox electricityTariff = new TextBox();

        TextBox gasOld = new TextBox();
        TextBox gasNew = new TextBox();
        TextBox gasTariff = new TextBox();

        Button calculateButton = new Button();

        DataGridView table = new DataGridView();

        Label totalLabel = new Label();

        public Form1()
        {
            Text = "Оплата комунальних послуг";
            Width = 900;
            Height = 600;

            StartPosition = FormStartPosition.CenterScreen;

            // Заголовки
            Label waterLabel = new Label();
            waterLabel.Text = "Вода";
            waterLabel.Location = new Point(50, 30);

            Label electricityLabel = new Label();
            electricityLabel.Text = "Світло";
            electricityLabel.Location = new Point(50, 100);

            Label gasLabel = new Label();
            gasLabel.Text = "Газ";
            gasLabel.Location = new Point(50, 170);

            // Поля вода
            waterOld.Location = new Point(150, 25);
            waterNew.Location = new Point(280, 25);
            waterTariff.Location = new Point(410, 25);

            // Поля світло
            electricityOld.Location = new Point(150, 95);
            electricityNew.Location = new Point(280, 95);
            electricityTariff.Location = new Point(410, 95);

            // Поля газ
            gasOld.Location = new Point(150, 165);
            gasNew.Location = new Point(280, 165);
            gasTariff.Location = new Point(410, 165);

            // Підказки
            waterOld.PlaceholderText = "Було";
            waterNew.PlaceholderText = "Стало";
            waterTariff.PlaceholderText = "Тариф";

            electricityOld.PlaceholderText = "Було";
            electricityNew.PlaceholderText = "Стало";
            electricityTariff.PlaceholderText = "Тариф";

            gasOld.PlaceholderText = "Було";
            gasNew.PlaceholderText = "Стало";
            gasTariff.PlaceholderText = "Тариф";

            // Кнопка
            calculateButton.Text = "Розрахувати";
            calculateButton.Location = new Point(50, 230);
            calculateButton.Width = 150;
            calculateButton.Height = 40;

            calculateButton.Click += Calculate;

            // Таблиця
            table.Location = new Point(50, 290);
            table.Width = 700;
            table.Height = 180;

            table.ColumnCount = 4;

            table.Columns[0].Name = "Послуга";
            table.Columns[1].Name = "Витрачено";
            table.Columns[2].Name = "Тариф";
            table.Columns[3].Name = "Сума";

            // Загальна сума
            totalLabel.Text = "Загальна сума: 0 грн";
            totalLabel.Location = new Point(50, 490);
            totalLabel.AutoSize = true;
            totalLabel.Font = new Font("Arial", 14, FontStyle.Bold);

            // Додаємо елементи
            Controls.Add(waterLabel);
            Controls.Add(electricityLabel);
            Controls.Add(gasLabel);

            Controls.Add(waterOld);
            Controls.Add(waterNew);
            Controls.Add(waterTariff);

            Controls.Add(electricityOld);
            Controls.Add(electricityNew);
            Controls.Add(electricityTariff);

            Controls.Add(gasOld);
            Controls.Add(gasNew);
            Controls.Add(gasTariff);

            Controls.Add(calculateButton);
            Controls.Add(table);
            Controls.Add(totalLabel);
        }

        private void Calculate(object? sender, EventArgs e)
        {
            double waterOldValue = double.Parse(waterOld.Text);
            double waterNewValue = double.Parse(waterNew.Text);
            double waterTariffValue = double.Parse(waterTariff.Text);

            double electricityOldValue = double.Parse(electricityOld.Text);
            double electricityNewValue = double.Parse(electricityNew.Text);
            double electricityTariffValue = double.Parse(electricityTariff.Text);

            double gasOldValue = double.Parse(gasOld.Text);
            double gasNewValue = double.Parse(gasNew.Text);
            double gasTariffValue = double.Parse(gasTariff.Text);

            // Витрачені показники
            double waterUsed = waterNewValue - waterOldValue;
            double electricityUsed = electricityNewValue - electricityOldValue;
            double gasUsed = gasNewValue - gasOldValue;

            // Вартість
            double waterCost = waterUsed * waterTariffValue;
            double electricityCost = electricityUsed * electricityTariffValue;
            double gasCost = gasUsed * gasTariffValue;

            // Очищення таблиці
            table.Rows.Clear();

            // Додавання результатів
            table.Rows.Add(
                "Вода",
                waterUsed,
                waterTariffValue,
                waterCost
            );

            table.Rows.Add(
                "Світло",
                electricityUsed,
                electricityTariffValue,
                electricityCost
            );

            table.Rows.Add(
                "Газ",
                gasUsed,
                gasTariffValue,
                gasCost
            );

            // Загальна сума
            double total = waterCost + electricityCost + gasCost;

            totalLabel.Text = $"Загальна сума: {total:F2} грн";
        }
    }
}