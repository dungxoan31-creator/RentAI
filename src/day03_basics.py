# kiểu số
area = 60
base_price_per_sqm = 20000000
total_price = area * base_price_per_sqm

# kiểu chuỗi
district = "Quận 1"
address = "123 Đường ABC, Phường XYZ, " + district

# kiểu boolean
is_available = True
has_garage = False

#in kiểu danh sách
print(type(area), type(base_price_per_sqm ), type(total_price))            # <class 'int'>
print(type(district), type(address))                                        # <class 'str'>
print(type(is_available), type(has_garage))   


# toán tử cơ bản
estimated_price = area * base_price_per_sqm
print("Estimated Price:", estimated_price)  


# Danh sách căn hộ (list các dict)
listings = [
    {"area": 40, "bedrooms": 1, "bathrooms": 1, "furnished": "basic"},
    {"area": 60, "bedrooms": 2, "bathrooms": 1, "furnished": "full"},
    {"area": 80, "bedrooms": 3, "bathrooms": 2, "furnished": "none"},
]

print("Số căn hộ:", len(listings))
print("Căn đầu tiên:", listings[0])
print("Phòng ngủ căn 2:", listings[1]["bedrooms"])

# Vòng lặp duyệt danh sách
for i, item in enumerate(listings, start=1):
    print(f"Căn {i}: {item['area']}m² - {item['bedrooms']}PN - {item['bathrooms']}WC - {item['furnished']}")
