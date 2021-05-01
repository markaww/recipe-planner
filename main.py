from p_email.m_send import send_email

def main():
    print("running script...")
    schedule.every().saturday.at("15:00").do(send_email)

    while True:
        schedule.run_pending()
        time.sleep(1)
    print("script complete, check your email!")

if __name__ == '__main__':
    main()