namespace MyWinFormsApp
{
    partial class Form1
    {
        private System.ComponentModel.IContainer components = null;

        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        private void InitializeComponent()
        {
            this.SuspendLayout();
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 600);
            this.Name = "Form1";
            this.Text = "Form1";
            this.BackColor = System.Drawing.Color.FromArgb(37, 37, 38);
            this.ForeColor = System.Drawing.Color.FromArgb(204, 204, 204);
            // 
            // textbox1
            // 
            this.textbox1 = new System.Windows.Forms.TextBox();
            this.textbox1.Location = new System.Drawing.Point(258, 182);
            this.textbox1.Name = "textbox1";
            this.textbox1.Size = new System.Drawing.Size(272, 77);
            this.textbox1.TabIndex = 0;
            this.textbox1.ForeColor = System.Drawing.Color.FromArgb(204, 204, 204);
            this.textbox1.BackColor = System.Drawing.Color.FromArgb(30, 30, 30);
            this.textbox1.Text = "CH1$lO";
            this.Controls.Add(this.textbox1);
            // 
            // button1
            // 
            this.button1 = new System.Windows.Forms.Button();
            this.button1.Location = new System.Drawing.Point(294, 291);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(153, 55);
            this.button1.TabIndex = 0;
            this.button1.ForeColor = System.Drawing.Color.FromArgb(204, 204, 204);
            this.button1.BackColor = System.Drawing.Color.FromArgb(51, 51, 51);
            this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button1.Text = "Бажаю Здоров'я";
            this.Controls.Add(this.button1);
            // 
            // label1
            // 
            this.label1 = new System.Windows.Forms.Label();
            this.label1.Location = new System.Drawing.Point(150, 400);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(100, 30);
            this.label1.TabIndex = 0;
            this.label1.ForeColor = System.Drawing.Color.FromArgb(204, 204, 204);
            this.label1.BackColor = System.Drawing.Color.Transparent;
            this.label1.Text = "Label";
            this.Controls.Add(this.label1);
            // 
            // label2
            // 
            this.label2 = new System.Windows.Forms.Label();
            this.label2.Location = new System.Drawing.Point(322, 399);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(100, 30);
            this.label2.TabIndex = 0;
            this.label2.ForeColor = System.Drawing.Color.FromArgb(204, 204, 204);
            this.label2.BackColor = System.Drawing.Color.Transparent;
            this.label2.Text = "Label";
            this.Controls.Add(this.label2);
            // 
            // label3
            // 
            this.label3 = new System.Windows.Forms.Label();
            this.label3.Location = new System.Drawing.Point(507, 400);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(100, 30);
            this.label3.TabIndex = 0;
            this.label3.ForeColor = System.Drawing.Color.FromArgb(204, 204, 204);
            this.label3.BackColor = System.Drawing.Color.Transparent;
            this.label3.Text = "Label";
            this.Controls.Add(this.label3);
            // 
            // Form controls collection
            // 
            this.Controls.AddRange(new System.Windows.Forms.Control[] {
                this.textbox1,
                this.button1,
                this.label1,
                this.label2,
                this.label3
            });
            this.ResumeLayout(false);
        }

        #endregion

        // Control declarations
        private System.Windows.Forms.TextBox textbox1;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
    }
}