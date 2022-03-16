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
log_nickname_banned = (
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
components_log_join = "<@{user}> joined. (age={age}, risk={risk})"