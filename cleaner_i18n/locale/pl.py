helloworld = "Witaj świecie!"
log_delete_success = "Wiadomośc została usunięta przez <@{user}> na kanale <#{channel}>."
log_delete_failure = (
    "Próba usunięcia wiadomości użytkownika <@{user}> na kanale <#{channel}> nie "
    "udała się z powodu braku permisji."
)
log_nickname_reset_success = "Zresetowano nazwę użytkownika <@{user}>."
log_nickname_reset_failure = (
    "Próba zresetowania nazwy użytkownika <@{user}> nie udała się z powodu braku "
    "permisji."
)
log_nickname_kick = (
    "Wyrzucono użytkownika <@{user}> ponieważ nie udało mi się zresetować jego nicku "
    "z powodu ratelimitu."
)
log_nickname_ban = (
    "Zbanowano użytkownika <@{user}> ponieważ nie udało mi się zresetować jego nicku "
    "z powodu ratelimitu."
)
log_nickname_failure = "Próba zresetowania nazwy użytkownika <@{user}> nie udała się z powodu ratelimitu"
log_challenge_failure = (
    "Próba sprawdzenia użytkownika <@{user}> nie udała się z powodu braku permisji "
    "lub ratelimitu."
)
log_challenge_timeout = "Nadano karę użytkownikowi <@{user}>."
log_challenge_role = "<@{user}> został odesłany do sprawdzenia."
log_challenge_kick = "<@{user}> został wyrzucony."
log_challenge_ban = "<@{user}> został zbanowany."
log_announcement_failure = "Nie mogłem wysyłać wiadomości na kanale <#{channel}>."
log_channelratelimit_success = (
    "Ustawiono tryb wolny na kanale <#{channel}> do {ratelimit} sekund."
)
log_embed_deleted = "Usunięto wiadomość"
log_embed_channel = "Kanał"
log_embed_sticker = "Naklejka"
components_antispam = "Wywołano ochronę: `{mitigation}`"
components_antispam_announcement = (
    ":warning: **Wykryto spam!**\n"
    "Wysyłanie tej samej wiadomści, lub wysyłanie kilku wiadomości w którtkim "
    "przedziale czasowym spowoduje nałożeniem kary."
)
components_dehoist = "Automatyczny dehoisting"
components_discordimpersonation = "Próba podszywania się pod administracje Discord."
components_firewall = "Wywołano zasadę firewall: `{rule}`"
components_firewall_phishing_content = (
    "Hej <@{user}>, prosimy o nie wysyłanie wiadomości z linkami do wyłudzania informacji."
)
components_firewall_phishing_domain_blacklisted = components_firewall_phishing_content
components_firewall_phishing_domain_heuristic = components_firewall_phishing_content
components_firewall_phishing_embed = components_firewall_phishing_content
components_firewall_ping_users_many = "Hej <@{user}>, prosimy o nie pingowanie tylu osób."
components_firewall_ping_users_few = "Hej <@{user}>, prosimy o nie pingowanie kilku osób na raz."
components_firewall_ping_roles = "Hej <@{user}>, prosimy o nie pingowanie tylu rol."
components_firewall_ping_broad = "Hej <@{user}>, prosimy o nie pingowanie @everyone oraz @here."
components_firewall_ping_hidden = (
    "Hej <@{user}>, prosimy o nie pingowanie osób przy użyciu błędów klienta Discord."
)
components_firewall_advertisement_discord_server = (
    "Hej <@{user}>, prosimy o nie wysyłanie zaproszeń do innych serwerów Discord."
)
components_firewall_emoji_mass = "Hej <@{user}>, prosimy o nie wysyłanie tylu emotek."
components_firewall_selfbot_embed = "Hej <@{user}>, prosimy o nie używanie selfbotów."
components_log_join = "<@{user}> dołączył. (Wiek={age}, Ryzyko={risk})"
slash_about_website = "Strona Internetowa"
slash_about_documentation = "Dokumentacja"
slash_about_blog = "Blog"
slash_about_privacy = "Polityka prywatności"
slash_about_terms = "Warunki usługi"
slash_about_impressum = "Impressum"
slash_about_discord = "Serwer pomocniczy"
slash_about_content = (
    "The Cleaner jest botem do Discorda zaprojektowany do utrzymywania twojego serwera "
    "w czystości i bezpieczeńswie."
)
slash_dashboard_guildonly = ":x: Ta komenda może zostać użyta tylko w serwerze."
slash_dashboard_dashboard = "Dashboard"
slash_dashboard_note = (
    ":warning: Nie posiadasz permisji `Administrator` lub `Zarządzanie serwerem`, "
    "więc nie możesz otrzymać dostępu do tego serwera."
)
slash_dashboard_content = (
    "Kliknij przycisk poniżej aby dostać się do konfiguracji serwera!"
)
slash_login_content = (
    ":warning: **Nie podawaj tego linku NIKOMU** :warning:\n"
    "Udostępnianie tego linku skutkuje dostępem do wszystkich ustawień The Cleaner'a!"
    "\n\n"
    "**Q:** Do czego jest ta funkcja w takim razie?\n"
    "**A:** Żebyś nie musiał cały czas się logować przy użyciu loginu i hasła na telefonie "
    "co może sprawiać niektórym problem."
)
slash_login_proceed = "Rozumiem niebezpieczeńswto, kontynuuj."
slash_login_nosession = (
    "Nie masz żadnych aktywnych sesjii, zaloguj się na początku w swojej przeglądarce"
)
slash_login_success = (
    "Użyj tego linku do zalogowania się.\n"
    "**Nie udostępniaj tego linku NIKOMU**.\n"
    "Nasza pomoc techniczna **NIGDY** nie zapyta o ten link."
)
slash_internal_error = (
    "**Błąd wewnętrzny**: Coś poszło nie tak na naszym końcu.\nProszę skontaktuj się z pomocą."
)
challenge_internal_error = slash_internal_error
challenge_discord = "Wspomóż"
challenge_action_give = "daj"
challenge_action_take = "zabierz"
challenge_no_settings = (
    "**Błąd wewnętrzny**: Nie mamy żadnych informacji na temat serwera w którym aktualnie "
    "jesteś.\n"
    "To powinno się naprawić w przeciągu kilku minut, skontaktuj się z pomocą jeśli po tym czasie "
    "nie działa."
)
challenge_disabled = "Interaktywne wyzwania zostały wyłączone przez administracje serwera."
challenge_no_role = (
    "Administracja serwera nie wybrała roli którą mam zarządzać.\n"
    "Skontaktuj się z administracją serwera w celu dokończenia konfiguracji."
)
challenge_already_verified = "Jesteś już zweryfikowany."
challenge_role_gone = (
    "Nie mogę znaleźć roli którą mam zarządzać. Może została usunięta?"
    "\nSkontaktuj się z administracją serwera aby dodali nową rolę."
)
challenge_role_managed = (
    "Nie mogę zarządzać rolą <&{role}> ponieważ jest ona zarządzana integracją.\n"
    "Skontaktuj się z administracją serwera aby zmienili na rolę która nie jest zarządzana."
)
challenge_role_everyone = (
    "Nie mogę zarządzać rolą everyone.\n"
    "Skontaktuj się z administracją serwera aby zmienili na inną rolę."
)
challenge_no_myself = (
    "**Błąd wewnętrzny**: Nie mogę siebie znaleźć.\n"
    "To powinno się naprawić w przeciągu kilku minut, skontaktuj się z pomocą jeśli po tym czasie "
    "nie działa."
)
challenge_hierarchy_link = "Hierarchia roli"
challenge_hierarchy = (
    "Rola którą powinieniem zarządzać jest wyżej odemnie, "
    "przez co nie mogę nią manipulować.\n"
    "Skontaktuj się z administracją serwera aby przesunęli moją rolę nad <&{role}> "
    "w ustawienaich roli."
)
challenge_no_perms = (
    "Nie mam permisji do zarządzania tą rolą :slight_frown:\n"
    "Skontaktuj się z administracją serwera aby dali mi uprawnienia `Administrator` lub "
    "`Zarządzanie serwerem`."
)
challenge_link = "Rozwiąż zagadkę"
challenge_content = (
    "Kliknij w przycisk poniżej i postępuj zgodnie z instrukcjami na stronie aby się "
    "zweryfikować.\n"
    "*Masz 5 minut zanim link się unieważni*"
)
challenge_verified = "Zostałeś zweryfikowany."
challenge_embed_title = "Potrzebna weryfikacja"
challenge_embed_description = (
    "Proszę zweryfikować że nie jesteś robotem.\nZacznij klikając w przycisk poniżej."
)
challenge_embed_verify = "Zweryfikuj"
challenge_embed_privacy = "Polityka prywatoności"