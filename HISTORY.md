# mellow-wombat history

### 14 August 2026
- mastodon NOAA WX collection to verify hardware
- wombat4 ran NOAA WX on all RTL-SDR collectors, variation in peaker count
- RTL-SDR dongles cannot use the original RTL-SDR library.
- investigating capybara survey using dumpvdl2 causes host reboot

### 10 August 2026
- Capybara collection starts, requires survey to discover active ACARS channels

### 26 July 2026
- Add Coyote reporting example, writes uptime to BlueSky
- wombat01 collector provisioning in progress
- wombat01 now powers all odroid, multicoupler via common 12VDC power
- wombat01 pi3c now has sense HAT for environment collection
- wombat04 refactor complete, restored to outside antenna and crate
- heeler wombat_docker and peccary_docker containers now built via gitlab runners when tagged
- hyena wombat_docker and peccary_docker containers now built via gitlab runners when tagged
- mastodon now uses pandas for peaker discovery
- heeler, hyena, mastodon now use json schema
