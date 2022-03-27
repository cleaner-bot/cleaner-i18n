helloworld = "Hallo Welt!"
log_delete_success = "Nachricht von <@{user}> in <#{channel}> gelöscht."
log_delete_failure = (
    "Konnte eine Nachricht von <@{user}> in <#{channel}> nicht löschen, "
    "weil mir Berechtigungen fehlen."
)
log_nickname_reset_success = "Nickname von <@{user}> zurückgesetzt."
log_nickname_reset_failure = (
    "Konnte den Nickanmen von <@{user}> nicht zurücksetzen, weil mir "
    "Berechtigungen fehlen."
)
log_nickname_kick = (
    "Habe <@{user}> gekickt, weil ich seinen Namen wegen Ratenlimits nicht "
    "zurücksetzen konnte."
)
log_nickname_ban = (
    "Habe <@{user}> verbannt, weil ich seinen Namen wegen Ratenlimits nicht "
    "zurücksetzen konnte."
)
log_nickname_failure = (
    "Konnte den Nicknamen von <@{user}> wegen Ratenlimits nicht zurücksetzen."
)
log_challenge_failure = (
    "Konnte <@{user}> nicht Herausfordern wegen fehlenden Berechtigungen "
    "oder Ratenlimits."
)
log_challenge_timeout = "Habe <@{user}> zur Bestrafung in Auszeit gesetzt."
log_challenge_role = "Habe <@{user}> herausgefordert."
log_challenge_kick = "Habe <@{user}> gekickt."
log_challenge_ban = "Habe <@{user}> verbannt."
log_announcement_failure = "Kann keine Nachricht in <#{channel}> senden."
log_channelratelimit_success = (
    "Slow-modus in <#{channel}> zu {ratelimit} Sekunden geändert."
)
log_embed_deleted = "Gelöschte Nachricht"
log_embed_channel = "Kanal"
log_embed_sticker = "Sticker"
components_antispam = "Antispam ausgelöst: `{mitigation}`"
components_antispam_announcement = (
    ":warning: **Spam erkannt!**\n"
    "Das Senden von der gleichen oder ähnlichen Nachrichten in einen kurzen "
    "Zeitraum wird bestraft."
)
components_dehoist = "Automatisches enthoisten."
components_impersonation_discord = "Versuchte Discord Angestellte zu imitieren."
components_firewall = "Firewall Regel ausgelöst: `{rule}`"
components_firewall_phishing_content = (
    "Hey <@{user}>, bitte sende keine Nachrichten die wahrscheinlich Phishing sind."
)
components_firewall_phishing_domain_blacklisted = components_firewall_phishing_content
components_firewall_phishing_domain_heuristic = components_firewall_phishing_content
components_firewall_phishing_embed = components_firewall_phishing_content
components_firewall_ping_users_many = (
    "Hey <@{user}>, bitte erwähne nicht so viele Nutzer."
)
components_firewall_ping_users_few = (
    "Hey <@{user}>, bitte erwähne nicht so mehrere Nutzer."
)
components_firewall_ping_roles = "Hey <@{user}>, bitte erwähne nicht so viele Rollen."
components_firewall_ping_broad = (
    "Hey <@{user}>, bitte erwähne nicht @everyone oder @here."
)
components_firewall_ping_hidden = (
    "Hey <@{user}>, bitte erwähne nicht andere Nutzer und nutze Clientfehler aus."
)
components_firewall_advertisement_discord_server = (
    "Hey <@{user}>, bitte sende keine Einladungen zu Discord servern."
)
components_firewall_emoji_mass = "Hey <@{user}>, bitte sende nicht so viele Emojis."
components_firewall_selfbot_embed = "Hey <@{user}>, bitte selfbotte nicht."
components_log_join = "<@{user}> tritt bei. (age={age}, risk={risk})"
slash_about_website = "Webseite"
slash_about_documentation = "Dokumentation"
slash_about_blog = "Blog"
slash_about_privacy = "Datenschutzerklärung"
slash_about_terms = "Allgemeine Geschäftsbedingungen"
slash_about_impressum = "Impressum"
slash_about_discord = "Support Server"
slash_about_content = (
    "The Cleaner ist ein Discord bot, der deinen Server sauber und sicher hält."
)
slash_dashboard_guildonly = ":x: Du kannst diesen Befehl nur in einen Server nutzen."
slash_dashboard_dashboard = "Dashboard"
slash_dashboard_note = (
    ":warning: Dir fehlt die `ADMINISTRATOR` oder `SERVER VERWALTEN` Berechtigung "
    "um auf das Dashboard zuzugreifen."
)
slash_dashboard_content = (
    "Nutze den unteren Link um zum Dashboard dieses Servers zu gehen!"
)
slash_login_content = (
    ":warning: **Geben diesen link zu NIEMANDEN!** :warning:\n"
    "Dieser link gibt jeden vollen zugriff auf die Einstellungen von The Cleaner!"
    "\n\n"
    "**Q:** Warum gibt es diesen Befehl?\n"
    "**A:** Damit du nicht auf deinem Handy im Browser anmelden musst."
)
slash_login_proceed = "Ich nutze den Link nur selbst, weiter."
slash_login_nosession = (
    "Du musst dich mindestenz einmal die Woche auf der Website manual anmelden."
)
slash_login_success = (
    "Nutze den unteren Link zum einloggen.\n"
    "**Teile diesen Link mit NIEMANDEN**.\n"
    "Unser Support team fragt **NIEMALS** nach diesem Link."
)
slash_internal_error = (
    "**Interner Fehler**: Irgendwas ging schief bei uns.\n"
    "Bitte kontaktiere unseren Support."
)
challenge_internal_error = slash_internal_error
challenge_discord = "Support"
challenge_action_give = "gebe"
challenge_action_take = "nehme"
challenge_no_settings = (
    "**Interner Fehler**: Wir haben keinen Informationen über den Serven in dem "
    "du bist.\nDies sollte sich nach ein paar Minuten von selbst beheben, "
    "falls nicht kontaktiere Support."
)
challenge_disabled = "Interaktive Herausforderungen wurden vom Server Team deaktiviert."
challenge_no_role = (
    "Das Server Team hat keine Rolle ausgewählt die ich {action}n soll.\n"
    "Kontaktiere das Server Team und weise sie darauf hin."
)
challenge_already_verified = "You are already verified."
challenge_role_gone = (
    "Ich kann die Role die ich {action}n soll nicht finden. "
    "Vielleicht wurde sie gelöscht?\n"
    "Kontaktiere das Server Team und weise sie darauf hin eine neue Rolle auszuwählen."
)
challenge_role_managed = (
    "Ich kann die Rolle <@&{role}> nicht {action}n, weil sie von einer "
    "Integration kontrolliert wird.\nKontaktiere das Server Team und weise sie darauf "
    "hin eine andere Rolle auszuwählen."
)
challenge_role_everyone = (
    "Ich kann die everyone Rolle nicht {action}n.\n"
    "Kontaktiere das Server Team und weise sie darauf hin eine andere Rolle "
    "auszuwählen."
)
challenge_no_myself = (
    "**Interner Fehler**: Ich finde mich selbst nicht.\n"
    "Dies sollte sich nach ein paar Minuten von selbst beheben, "
    "falls nicht kontaktiere Support."
)
challenge_hierarchy_link = "Role hierarchy"
challenge_hierarchy = (
    "Die Rolle, die ich {action}n soll, ist über mir in der Rollen Hierarchie, "
    "und kann sie deswegen nicht {action}n."
    "Kontaktiere das Server Team und weise sie darauf hin mich über die "
    "<@&{role}> Rolle zu platzieren."
)
challenge_no_perms = (
    "Ich habe nicht das Recht um Rollen zu {action}n:slight_frown:\n"
    "Kontaktiere das Server Team und weise sie darauf hin mir das `ADMINISTRATOR` "
    "oder `ROLLEN VERWALTEN` Berechtigung zu geben."
)
challenge_link = "Herausforderunng lösen"
challenge_content = (
    "Klicke den Knopf und folge den Anweisungen auf der Webseite um dich zu "
    "Verifizieren.\n*Der Link wird nach 5 Minuten ungültig*"
)
challenge_verified = "Du wurdest verifiziert."
challenge_embed_title = "Verifizierung benötigt."
challenge_embed_description = (
    "Bitte verifizieren, dass du kein Roboter bist.\n"
    "Klicke den unteren Knopf um zu beginnen."
)
challenge_embed_verify = "Verifizieren"
challenge_embed_privacy = "Datenschutzerklärung"
