helloworld = "Hello World!"
log_delete_success = "Deleted message by <@{user}> in <#{channel}>."
log_delete_failure = (
    "Failed to delete message by <@{user}> in <#{channel}> due to missing permissions."
)
log_nickname_reset_success = "Reset <@{user}>'s nickname."
log_nickname_reset_failure = (
    "Failed to reset <@{user}>'s nickname due to missing permissions."
)
log_nickname_kick = (
    "Kicked <@{user}> because I failed to reset their nickname due to ratelimits."
)
log_nickname_ban = (
    "Banned <@{user}> because I failed to reset their nickname due to ratelimits."
)
log_nickname_failure = "Failed to reset <@{user}>'s nickname due to ratelimits."
log_challenge_failure = (
    "Failed to challenge <@{user}> due to missing permissions or ratelimits."
)
log_challenge_timeout = "Put <@{user}> in timeout as challenge."
log_challenge_role = "<@{user}> has been challenged."
log_challenge_kick = "<@{user}> has been kicked."
log_challenge_ban = "<@{user}> has been banned."
log_announcement_failure = "Unable to send a message in <#{channel}>."
log_channelratelimit_success = (
    "Adjusted slowmode in <#{channel}> to {ratelimit} seconds."
)
components_antispam = "Triggered antispam: `{mitigation}`"
components_antispam_announcement = (
    ":warning: **Spam detected!**\n"
    "Sending the same message or sending multiple messages in a short time "
    "frame will result in a punishment."
)
components_dehoist = "Automatic dehoisting"
components_discordimpersonation = "Tried impersonating Discord staff."
components_firewall = "Triggered firewall rule: `{rule}`"
components_firewall_phishing_content = "Hey <@{user}>, please don't post content that is likely to be phishing."
components_firewall_phishing_domain_blacklisted = components_firewall_phishing_content
components_firewall_phishing_domain_heuristic = components_firewall_phishing_content
components_firewall_phishing_embed = components_firewall_phishing_content
components_firewall_ping_users_many = "Hey <@{user}>, please don't ping many users."
components_firewall_ping_users_few = "Hey <@{user}>, please don't ping multiple users."
components_firewall_ping_roles = "Hey <@{user}>, please don't ping multiple roles."
components_firewall_ping_broad = "Hey <@{user}>, please don't ping @everyone or @here."
components_firewall_ping_hidden = "Hey <@{user}>, please don't try to ping others while abusing client bugs."
components_firewall_ping_advertisement_discord_server = "Hey <@{user}>, please don't send invites to Discord servers."
components_firewall_emoji_mass = "Hey <@{user}>, please don't send soo many emojis."
components_firewall_selfbot_embed = "Hey <@{user}>, please don't selfbot."
components_log_join = "<@{user}> joined. (age={age}, risk={risk})"
