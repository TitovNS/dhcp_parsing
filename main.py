import csv


def csv_read():
    with open('dhcp.csv', newline='') as File:
        return csv.reader(File)
        # for row in reader:
        #     if row[5] == '':
        #         print(f'add mac-address={row[4]} address={row[0]} server=dhcp1')
        #     else:
        #         print(f'add mac-address={row[4]} address={row[0]} server=dhcp1 comment="{row[5]}"')


def write_script_for_mikrotik(dhcp_list):
    with open(r'E:\!Nikita\RPA\python\dhcp_parsing\dhcp.txt', 'w') as File:
        for row in dhcp_list:
            File.write(f'add mac-address={row[4]} address={row[0]} server=dhcp1 comment={row[5]}\n')


if __name__ == '__main__':
    dhcp_list = csv_read()
    write_script_for_mikrotik(dhcp_list)
