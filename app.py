import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('AliExpress PPN Calculator')

        # Create the input field and label
        self.product_price_label = ttk.Label(self.root, text='Product Price:')
        self.product_price_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.product_price_entry = ttk.Entry(self.root)
        self.product_price_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create the calculate button
        self.calculate_button = ttk.Button(self.root, text='Calculate', command=self.calculate_price)
        self.calculate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Create the result labels
        self.bea_masuk_impor_label = ttk.Label(self.root, text='Bea Masuk Impor:', anchor=tk.W)
        self.bea_masuk_impor_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.bea_masuk_impor_value_label = ttk.Label(self.root, text='Rp 0', anchor=tk.W, justify=tk.LEFT)
        self.bea_masuk_impor_value_label.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.ppn_impor_label = ttk.Label(self.root, text='PPN Impor:', anchor=tk.W)
        self.ppn_impor_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.ppn_impor_value_label = ttk.Label(self.root, text='Rp 0', anchor=tk.W, justify=tk.LEFT)
        self.ppn_impor_value_label.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.biaya_admin_pos_label = ttk.Label(self.root, text='Biaya Admin Pos:', anchor=tk.W)
        self.biaya_admin_pos_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
        self.biaya_admin_pos_value_label = ttk.Label(self.root, text='Rp 15,000', anchor=tk.W, justify=tk.LEFT)
        self.biaya_admin_pos_value_label.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.handling_fee_label = ttk.Label(self.root, text='Handling Fee:', anchor=tk.W)
        self.handling_fee_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
        self.handling_fee_value_label = ttk.Label(self.root, text='Rp 30,000', anchor=tk.W, justify=tk.LEFT)
        self.handling_fee_value_label.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.ppn_admin_pos_label = ttk.Label(self.root, text='PPN Admin Pos:', anchor=tk.W)
        self.ppn_admin_pos_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
        self.ppn_admin_pos_value_label = ttk.Label(self.root, text='Rp 0', anchor=tk.W, justify=tk.LEFT)
        self.ppn_admin_pos_value_label.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        self.final_ppn_label = ttk.Label(self.root, text='Final PPN:', font=('TkDefaultFont', 12, 'bold'), anchor=tk.W)
        self.final_ppn_label.grid(row=7, column=0, padx=5, pady=5, sticky=tk.W)
        self.final_ppn_value_label = ttk.Label(self.root, text='Rp 0', font=('TkDefaultFont', 12), anchor=tk.W, justify=tk.LEFT)
        self.final_ppn_value_label.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.final_price_label = ttk.Label(self.root, text='Final Price:', font=('TkDefaultFont', 12, 'bold'), anchor=tk.W)
        self.final_price_label.grid(row=8, column=0, padx=5, pady=5, sticky=tk.W)
        self.final_price_value_label = ttk.Label(self.root, text='Rp 0', font=('TkDefaultFont', 12), anchor=tk.W, justify=tk.LEFT)
        self.final_price_value_label.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

        
        # Bind the <Return> key to the calculate method
        self.root.bind('<Return>', self.calculate_price)

        self.root.mainloop()

    def calculate_price(self, event=None):
        try:
            product_price = int(self.product_price_entry.get().replace(',', ''))
            # Update the calculation to handle the new tax rates
            bea_masuk_impor = round(0.075 * product_price / 1000) * 1000
            ppn_impor = round((product_price + bea_masuk_impor) * 0.11 / 1000) * 1000
            ppn_admin_pos = 15000 * 0.11
            final_ppn = bea_masuk_impor + ppn_impor + ppn_admin_pos + 15000 + 30000
            final_price = product_price + final_ppn

            # Update the result labels
            self.bea_masuk_impor_value_label.config(text=f'Rp {bea_masuk_impor:,.0f}')
            self.ppn_impor_value_label.config(text=f'Rp {ppn_impor:,.0f}')
            self.biaya_admin_pos_value_label.config(text='Rp 15,000')
            self.handling_fee_value_label.config(text='Rp 30,000')
            self.ppn_admin_pos_value_label.config(text=f'Rp {ppn_admin_pos:,.0f}')
            self.final_ppn_value_label.config(text=f'Rp {final_ppn:,.0f}')
            self.final_price_value_label.config(text=f'Rp {final_price:,.0f}')
        except ValueError:
            # Invalid input
            pass

if __name__ == '__main__':
    MainWindow()