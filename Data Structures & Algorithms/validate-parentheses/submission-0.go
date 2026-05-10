func isValid(s string) bool {

for strings.Contains(s, "()") || strings.Contains(s, "{}") || strings.Contains(s, "[]"){
	s = strings.ReplaceAll(s, "()", "")
	s = strings.ReplaceAll(s, "{}", "")
	s = strings.ReplaceAll(s, "[]", "")
}

if s == ""{
	return true
}
return false
}
