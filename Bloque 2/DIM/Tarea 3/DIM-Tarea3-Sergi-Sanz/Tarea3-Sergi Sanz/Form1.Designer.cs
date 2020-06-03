namespace REcoSample
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.label1 = new System.Windows.Forms.Label();
            this.imgJardin = new System.Windows.Forms.PictureBox();
            this.imgCasaVolver = new System.Windows.Forms.PictureBox();
            this.pizarra = new System.Windows.Forms.TextBox();
            this.ninos = new System.Windows.Forms.PictureBox();
            this.museo = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.imgJardin)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.imgCasaVolver)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.ninos)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.museo)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 28F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(34, 76);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(0, 44);
            this.label1.TabIndex = 0;
            // 
            // imgJardin
            // 
            this.imgJardin.BackColor = System.Drawing.Color.Transparent;
            this.imgJardin.Image = ((System.Drawing.Image)(resources.GetObject("imgJardin.Image")));
            this.imgJardin.Location = new System.Drawing.Point(0, -9);
            this.imgJardin.Name = "imgJardin";
            this.imgJardin.Size = new System.Drawing.Size(457, 312);
            this.imgJardin.TabIndex = 3;
            this.imgJardin.TabStop = false;
            this.imgJardin.Visible = false;
            // 
            // imgCasaVolver
            // 
            this.imgCasaVolver.BackColor = System.Drawing.Color.Transparent;
            this.imgCasaVolver.Image = ((System.Drawing.Image)(resources.GetObject("imgCasaVolver.Image")));
            this.imgCasaVolver.Location = new System.Drawing.Point(0, -1);
            this.imgCasaVolver.Name = "imgCasaVolver";
            this.imgCasaVolver.Size = new System.Drawing.Size(450, 304);
            this.imgCasaVolver.TabIndex = 4;
            this.imgCasaVolver.TabStop = false;
            this.imgCasaVolver.Visible = false;
            // 
            // pizarra
            // 
            this.pizarra.Dock = System.Windows.Forms.DockStyle.Bottom;
            this.pizarra.Font = new System.Drawing.Font("Lucida Sans", 15.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.pizarra.Location = new System.Drawing.Point(0, 300);
            this.pizarra.Multiline = true;
            this.pizarra.Name = "pizarra";
            this.pizarra.Size = new System.Drawing.Size(450, 84);
            this.pizarra.TabIndex = 105;
            this.pizarra.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // ninos
            // 
            this.ninos.BackColor = System.Drawing.Color.Transparent;
            this.ninos.Image = ((System.Drawing.Image)(resources.GetObject("ninos.Image")));
            this.ninos.Location = new System.Drawing.Point(53, 117);
            this.ninos.Name = "ninos";
            this.ninos.Size = new System.Drawing.Size(274, 152);
            this.ninos.TabIndex = 106;
            this.ninos.TabStop = false;
            this.ninos.Visible = false;
            // 
            // museo
            // 
            this.museo.BackColor = System.Drawing.Color.Transparent;
            this.museo.Image = ((System.Drawing.Image)(resources.GetObject("museo.Image")));
            this.museo.Location = new System.Drawing.Point(0, -1);
            this.museo.Name = "museo";
            this.museo.Size = new System.Drawing.Size(450, 304);
            this.museo.TabIndex = 107;
            this.museo.TabStop = false;
            this.museo.Visible = false;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.FloralWhite;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.ClientSize = new System.Drawing.Size(450, 384);
            this.Controls.Add(this.ninos);
            this.Controls.Add(this.pizarra);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.imgJardin);
            this.Controls.Add(this.museo);
            this.Controls.Add(this.imgCasaVolver);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.imgJardin)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.imgCasaVolver)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.ninos)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.museo)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.PictureBox imgJardin;
        private System.Windows.Forms.PictureBox imgCasaVolver;
        private System.Windows.Forms.TextBox pizarra;
        private System.Windows.Forms.PictureBox ninos;
        private System.Windows.Forms.PictureBox museo;
    }
}

