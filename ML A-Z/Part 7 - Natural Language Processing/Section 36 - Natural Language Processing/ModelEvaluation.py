class ModelEvaluation:
    cm = [2,2]
    def __init__(self, cm):
        self.cm = cm
    
    @staticmethod
    def get_TN(cm):
        return cm[0][0]
    
    @staticmethod
    def get_FN(cm):
        return cm[1][0]
    
    @staticmethod
    def get_TP(cm):
        return cm[1][1]
    
    @staticmethod
    def get_FP(cm):
        return cm[0][1]
    
    # Calc accuracy 
    # (TP + TN) / (TP + TN + FP + FN)
    def calc_accuracy(cm):    
        accuracy = (ModelEvaluation.get_TP(cm)+ get_TN(cm) ) / (get_TP(cm) + get_TN(cm) + get_FN(cm)  + get_FN(cm) )    
        return accuracy
    
    # Calc precision
    # TP / (TP + FP)
    def calc_precision(cm):
        precision = get_TP(cm) / (get_TP(cm) + get_FN(cm) )
        return precision
    
    # Calc recall
    # TP / (TP + FN)
    def calc_recall(cm):
        recall = get_TP(cm) / (get_TP(cm) + get_FN(cm) )
        return recall
    
    # Calc F1 Score
    # = 2 * Precision * Recall / (Precision + Recall)
    def calc_f1_score(cm):
        f1_score = (2 * calc_precision(cm) * calc_recall(cm)) / (calc_precision(cm) + calc_recall(cm))
        return f1_score