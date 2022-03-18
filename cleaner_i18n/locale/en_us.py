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
components_firewall_phishing_content = (
    "Hey <@{user}>, please don't post content that is likely to be phishing."
)
components_firewall_phishing_domain_blacklisted = components_firewall_phishing_content
components_firewall_phishing_domain_heuristic = components_firewall_phishing_content
components_firewall_phishing_embed = components_firewall_phishing_content
components_firewall_ping_users_many = "Hey <@{user}>, please don't ping many users."
components_firewall_ping_users_few = "Hey <@{user}>, please don't ping multiple users."
components_firewall_ping_roles = "Hey <@{user}>, please don't ping multiple roles."
components_firewall_ping_broad = "Hey <@{user}>, please don't ping @everyone or @here."
components_firewall_ping_hidden = (
    "Hey <@{user}>, please don't try to ping others while abusing client bugs."
)
components_firewall_advertisement_discord_server = (
    "Hey <@{user}>, please don't send invites to Discord servers."
)
components_firewall_emoji_mass = "Hey <@{user}>, please don't send soo many emojis."
components_firewall_selfbot_embed = "Hey <@{user}>, please don't selfbot."
components_log_join = "<@{user}> joined. (age={age}, risk={risk})"
slash_about_website = "Website"
slash_about_documentation = "Documentation"
slash_about_blog = "Blog"
slash_about_privacy = "Privacy Policy"
slash_about_terms = "Terms of Service"
slash_about_impressum = "Impressum"
slash_about_discord = "Support Server"
slash_about_content = (
    "The Cleaner is a Discord bot designed to keep your server clean and safe."
)
slash_dashboard_guildonly = ":x: This command can only be used in a server."
slash_dashboard_dashboard = "Dashboard"
slash_dashboard_note = (
    ":warning: You do not have the `ADMINISTRATOR` or `MANAGE SERVER` permission, "
    "so you can not access this server's dashboard."
)
slash_dashboard_content = (
    "Click the button below to go to the dashboard of this server!"
)
slash_internal_error = (
    "**Internal error**: Something went wrong on our end.\nPlease contact support."
)
challenge_internal_error = slash_internal_error
challenge_discord = "Support"
challenge_no_settings = (
    "**Internal error**: We have no information about the server you are in.\n"
    "This should fix itself after a few minutes, contact support if it does not."
)
challenge_disabled = "Interactive challenges have been disabled by the server staff."
challenge_no_role = (
    "Server staff has not selected a role for me {action}.\n"
    "Contact server staff and ask them that they have not yet completed the setup."
)
challenge_already_verified = "You are already verified."
challenge_role_gone = (
    "I can not find the role I am supposed to {action} you. Maybe it has been "
    "deleted?\nContact server staff and ask them to select an up-to-date role."
)
challenge_role_managed = (
    "I can not {action} the role <&{role}> because it is managed by an integration.\n"
    "Contact server staff and ask them to select a role that is not managed."
)
challenge_role_everyone = (
    "I can not {action} the everyone role.\n"
    "Contact server staff and ask them to select a different role."
)
challenge_no_myself = (
    "**Internal error**: I can not find myself.\n"
    "This should fix itself after a few minutes, contact support if it does not."
)
challenge_hierarchy_link = "Role hierarchy"
challenge_hierarchy = (
    "The role I am supposed to {action} is above me in the role hierarchy and "
    "therefore I can not {action} it.\n"
    "Contact server staff and ask them to move me above the <&{role}> role in "
    "the role settings."
)
challenge_no_perms = (
    "I do not have the permission to {action} roles :slight_frown:\n"
    "Contact server staff and ask them to give me the `ADMINISTRATOR` or "
    "`MANAGE ROLES` permission."
)
challenge_link = "Solve challenge"
challenge_content = (
    "Click the button below and follow the instructions on the website to verify.\n"
    "*You have 5 minutes before the link becomes invalid*"
)
challenge_verified = "You have been verified."
challenge_embed_title = "Verification required"
challenge_embed_description = (
    "Please verify that you are not a robot.\nStart by clicking on the button below."
)
challenge_embed_verify = "Verify"
challenge_embed_privacy = "Privacy Policy"
