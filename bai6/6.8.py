class Bank:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.pin = "1234"  

    def verify_pin(self):
        """Kiểm tra mã PIN"""
        pin = input("Nhập mã PIN của bạn: ")
        if pin == self.pin:
            print("✅ Mã PIN đúng!\n")
            return True
        else:
            print("❌ Mã PIN sai! Vui lòng thử lại.\n")
            return False

    def show_menu(self):
        """Hiển thị menu lựa chọn"""
        while True:
            print("===== MENU ATM =====")
            print("1. Xem số dư")
            print("2. Rút tiền")
            print("3. Gửi tiền")
            print("4. Thoát")
            choice = input("Chọn chức năng (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                print("Cảm ơn đã sử dụng dịch vụ! Tạm biệt 👋")
                break
            else:
                print("❌ Lựa chọn không hợp lệ!\n")

    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance:,.0f} VND\n")

    def withdraw(self):
        amount = float(input("Nhập số tiền muốn rút: "))
        if amount <= 0:
            print("❌ Số tiền không hợp lệ!\n")
        elif amount > self.balance:
            print("❌ Số dư không đủ!\n")
        else:
            self.balance -= amount
            print(f"✅ Rút {amount:,.0f} VND thành công! Số dư mới: {self.balance:,.0f} VND\n")

    def deposit(self):
        amount = float(input("Nhập số tiền muốn gửi: "))
        if amount <= 0:
            print("❌ Số tiền không hợp lệ!\n")
        else:
            self.balance += amount
            print(f"✅ Gửi {amount:,.0f} VND thành công! Số dư mới: {self.balance:,.0f} VND\n")



bank_account = Bank("le van phong ", "123456789", 5000000)

print("Chào mừng đến với máy ATM mini 💳")
if bank_account.verify_pin():
    bank_account.show_menu()
