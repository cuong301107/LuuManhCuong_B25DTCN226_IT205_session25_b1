class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self._account_name = None
        self.__balance = 0
        self.account_name = account_name

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, new_name):
        if new_name is None:
            print("Tên tài khoản không được để trống")
            return
        cleaned = new_name.strip()
        if not cleaned:
            print("Tên tài khoản không được để trống")
            return
        self._account_name = cleaned.upper()

    @staticmethod
    def validate_account_number(account_number):
        return isinstance(account_number, str) and len(account_number) == 10 and account_number.isdigit()

    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        self.__balance += amount
        print(f"""
            Nạp tiền thành công: +{format(amount, ',')} VND
            Số dư mới: {format(self.__balance, ',')} VND
            """)

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return
        total = amount + self.__class__.transaction_fee
        if self.__balance < total:
            print(f"""
                Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch
                Số dư hiện tại: {format(self.__balance, ',')} VND
                """)
            return

        self.__balance -= total
        print(f"""
            Rút tiền thành công: -{format(amount, ',')} VND
            Phí giao dịch: {format(self.__class__.transaction_fee, ',')} VND
            Số dư mới: {format(self.__balance, ',')} VND
            """)

    def display_info(self):
        print(f"""
            --- THÔNG TIN TÀI KHOẢN ---
            Ngân hàng: {self.__class__.bank_name}
            Số tài khoản: {self.account_number}
            Tên chủ tài khoản: {self.account_name}
            Số dư hiện tại: {format(self.__balance, ',')} VND
            Phí giao dịch: {format(self.__class__.transaction_fee, ',')} VND
            """)


def main():
    current_account = None

    while True:
        print("""
            ===== VIETCOMBANK DIGIBANK SIMULATOR =====
            1. Mở tài khoản mới
            2. Xem thông tin tài khoản
            3. Giao dịch Nạp / Rút tiền
            4. Cập nhật Tên chủ tài khoản
            5. Đổi phí giao dịch hệ thống
            6. Thoát chương trình
            ==========================================
            """)

        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == "1":
            print("\n--- MỞ TÀI KHOẢN MỚI ---")
            while True:
                acc_number = input("Nhập số tài khoản 10 chữ số: ").strip()
                if not BankAccount.validate_account_number(acc_number):
                    print("""
                        Số tài khoản không hợp lệ!
                        Số tài khoản phải gồm đúng 10 chữ số.
                        """)
                    continue

                name = input("Nhập tên chủ tài khoản: ")
                temp_account = BankAccount(acc_number, name)

                if temp_account.account_name is None:
                    print("Tên tài khoản không được để trống")
                    continue

                current_account = temp_account
                print(f"""
                    Mở tài khoản thành công!
                    Số tài khoản: {current_account.account_number}
                    Tên chủ tài khoản: {current_account.account_name}
                    """)
                break

        elif choice == "2":
            if current_account is None:
                print("""
                    Hệ thống chưa có thông tin tài khoản
                    Vui lòng mở tài khoản ở Chức năng 1 trước.
                    """)
            else:
                current_account.display_info()

        elif choice == "3":
            if current_account is None:
                print("""
                    Hệ thống chưa có thông tin tài khoản
                    Vui lòng mở tài khoản ở Chức năng 1 trước.
                    """)
                continue

            print("""
                --- GIAO DỊCH NẠP / RÚT TIỀN ---
                1. Nạp tiền
                2. Rút tiền
                """)

            trans_choice = input("Chọn loại giao dịch (1-2): ").strip()
            if trans_choice not in ("1", "2"):
                print("Lựa chọn không hợp lệ")
                continue

            amount_input = input("Nhập số tiền giao dịch: ").strip()
            try:
                amount = int(amount_input)
            except ValueError:
                print("Số tiền giao dịch phải là số nguyên")
                continue

            if trans_choice == "1":
                current_account.deposit(amount)
            else:
                current_account.withdraw(amount)

        elif choice == "4":
            if current_account is None:
                print("""
                    Hệ thống chưa có thông tin tài khoản
                    Vui lòng mở tài khoản ở Chức năng 1 trước.
                    """)
                continue

            print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
            new_name = input("Nhập tên mới: ")
            old_name = current_account.account_name
            current_account.account_name = new_name

            if current_account.account_name == old_name:
                print("Tên tài khoản không được để trống")
            else:
                print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        elif choice == "5":
            print(f"""
                --- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---
                Phí giao dịch hiện tại: {format(BankAccount.transaction_fee, ',')} VND
                """)

            new_fee_input = input("Nhập phí giao dịch mới: ").strip()
            try:
                new_fee = int(new_fee_input)
            except ValueError:
                print(f"""
                    Phí giao dịch phải là số nguyên
                    Phí giao dịch hiện tại vẫn là {format(BankAccount.transaction_fee, ',')} VND
                    """)
                continue

            if new_fee < 0:
                print(f"""
                    Phí giao dịch không được âm
                    Phí giao dịch hiện tại vẫn là {format(BankAccount.transaction_fee, ',')} VND
                    """)
                continue

            BankAccount.update_transaction_fee(new_fee)
            print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {format(BankAccount.transaction_fee, ',')} VND")

        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()
