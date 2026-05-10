locals {
  bucket_name = "mellow-wombat.braingang.net"

  placeholder_prefixes = toset([
    "wombat/",
    "wombat/admin/",
    "heeler2/",
    "heeler2/fresh/",
    "heeler2/archive/",
  ])
}