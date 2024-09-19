import wx
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from config import api_token

# Initialize the LLM
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=api_token)

# Define the prompt template
template = "<s>[INST]Write long answer of</s>{question}[/INST]"
prompt_template = PromptTemplate.from_template(template)

class MyFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MyFrame, self).__init__(*args, **kw)
        
        self.InitUI()
        
    def InitUI(self):
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        self.response_text = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL)
        vbox.Add(self.response_text, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.input_text = wx.TextCtrl(panel)
        hbox.Add(self.input_text, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)
        
        submit_button = wx.Button(panel, label='Submit')
        submit_button.Bind(wx.EVT_BUTTON, self.OnSubmit)
        hbox.Add(submit_button, flag=wx.EXPAND)
        
        vbox.Add(hbox, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
        
        panel.SetSizer(vbox)
        
    def OnSubmit(self, event):
        user_question = self.input_text.GetValue()
        if user_question.lower() == "exit":
            self.Close()
        else:
            formatted_prompt_template = prompt_template.format(question=user_question)
            response = llm.stream(formatted_prompt_template)
            
            response_text = ""
            for res in response:
                response_text += res
            
            self.response_text.SetValue(response_text)
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, title="AI Response App", size=(1080, 720))
        frame.Show(True)
        return True

app = MyApp()
app.MainLoop()
