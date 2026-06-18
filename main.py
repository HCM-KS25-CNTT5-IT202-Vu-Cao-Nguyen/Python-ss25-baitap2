class NetflixAccount:
    """
    NetflixAccount class.

    Demonstrates:
    - Encapsulation
    - Class Attribute
    - Instance Attribute
    - Property
    - Static Method
    - Class Method
    """
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):

        self.email = email
        self.__password = ""
        self.__plan = "Basic"
        self.profiles = []

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, new_password):

        if len(new_password) < 6:
            raise ValueError("Password is too short")

        self.__password = new_password

    @property
    def plan(self):
        return self.__plan

    @staticmethod
    def validate_email(email):

        if "@" in email and "." in email:
            return True

        return False

    @classmethod
    def update_max_profiles(cls, new_limit):

        if new_limit <= 0:
            print("Số lượng Profile phải lớn hơn 0")
            return False

        cls.max_profiles = new_limit
        return True

    def add_profile(self, profile_name):

        profile_name = profile_name.strip()

        if profile_name == "":
            print("Tên Profile không được để trống")
            return False

        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này")
            return False

        self.profiles.append(profile_name)

        return True

    def upgrade_plan(self, new_plan):

        valid_plans = [
            "Basic",
            "Standard",
            "Premium"
        ]

        if new_plan not in valid_plans:

            print("Gói cước không hợp lệ")
            return False

        self.__plan = new_plan

        return True

    def display_info(self):

        print("\n========== ACCOUNT INFORMATION ==========")

        print(f"Platform : {NetflixAccount.platform_name}")

        print(f"Email    : {self.email}")

        print(f"Password : {self.password}")

        print(f"Plan     : {self.plan}")

        if len(self.profiles) == 0:
            print("Profiles : []")
        else:
            print("Profiles :")

            for index, profile in enumerate(self.profiles, start=1):
                print(f"{index}. {profile}")

        print(
            f"Maximum Profiles : "
            f"{NetflixAccount.max_profiles}"
        )


current_account = None

while True:

    print("\n===== NETFLIX ACCOUNT MANAGER =====")
    print("1. Đăng ký tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Thêm người xem")
    print("4. Nâng cấp gói cước")
    print("5. Cập nhật chính sách Netflix")
    print("6. Thoát chương trình")
    print("===================================")

    choice = input("Chọn chức năng (1-6): ")

    if choice == "1":

        print("\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")

        while True:

            email = input("Nhập Email: ")

            if NetflixAccount.validate_email(email):
                break

            print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")

        while True:

            password = input("Nhập mật khẩu: ")

            try:

                account = NetflixAccount(email)

                account.password = password

                current_account = account

                break

            except ValueError as e:

                print(e)

        print("\nĐăng ký tài khoản thành công!")

    elif choice == "2":

        if current_account is None:

            print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")

        else:

            current_account.display_info()

    elif choice == "3":

        if current_account is None:

            print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            continue

        print("\n--- THÊM PROFILE ---")

        profile_name = input("Nhập tên Profile: ")

        if current_account.add_profile(profile_name):

            print("Thêm Profile thành công!")

    elif choice == "4":

        if current_account is None:

            print("Vui lòng đăng ký tài khoản trước (Chức năng 1)")
            continue

        print("\n--- NÂNG CẤP GÓI CƯỚC ---")

        print("1. Basic")
        print("2. Standard")
        print("3. Premium")

        option = input("Chọn gói: ")

        if option == "1":
            plan = "Basic"

        elif option == "2":
            plan = "Standard"

        elif option == "3":
            plan = "Premium"

        else:

            print("Lựa chọn không hợp lệ.")
            continue

        if current_account.upgrade_plan(plan):

            print("Nâng cấp gói cước thành công!")
            print(f"Gói hiện tại: {current_account.plan}")

    elif choice == "5":

        print("\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---")

        print(
            f"Giới hạn hiện tại: "
            f"{NetflixAccount.max_profiles} Profile"
        )

        try:

            new_limit = int(
                input("Nhập giới hạn mới: ")
            )

        except ValueError:

            print("Giới hạn không hợp lệ.")
            continue

        if NetflixAccount.update_max_profiles(new_limit):

            print(
                "Đã cập nhật giới hạn Profile "
                f"toàn hệ thống thành "
                f"{NetflixAccount.max_profiles}"
            )
    elif choice == "6":

        print("\nCảm ơn bạn đã sử dụng Netflix Account Manager!")

        break
    else:

        print("Lựa chọn không hợp lệ.")